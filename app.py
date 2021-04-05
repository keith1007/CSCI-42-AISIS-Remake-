from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    session
)
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db_name = 'testdb.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.jinja_env.add_extension('jinja2.ext.do')
db = SQLAlchemy(app)

from models import (
    Announcement,
    FAQ,
    FaqCategory,
    EnlistmentUpdate,
    Student,
    Course,
    Section
)

@app.route('/')
def index():
    return redirect(url_for('announcements'))

@app.route('/announcements')
def announcements():
    return render_template(
        'AnnouncementsPage.html',
        announcements=Announcement.query.all()
    )

@app.route('/enlistment_updates')
def enlistment_updates():
    return render_template('EnlistmentUpdatesPage.html', updates=EnlistmentUpdate.query.all())

@app.route('/faq')
def faq():
    return render_template('FAQPage.html', faqs={category.name: FAQ.query.filter_by(category_id = category.id) for category in FaqCategory.query.all()})

@app.route('/student_portal')
def student_portal():
    return render_template('StudentPortalPage.html', student_info=Student.query.filter_by(id=session['username']).first())               

@app.route('/login', methods=['POST', 'GET'])
def login():
    possible_student = Student.query.filter_by(id = request.form['username']).first()
    if possible_student and possible_student.password ==  request.form['password']:
        session['username'] = request.form['username']
        session['login_failed'] = False
    if 'username' in session:
        return redirect(url_for('student_portal'))
    else:
        session['login_failed'] = True
        return redirect(url_for(request.referrer.split('/')[-1]))

@app.route('/logout')
def logout():
    prev_route = request.referrer.lstrip(request.url_root)
    if 'username' in session:
        session.pop('username')
    if prev_route.split('/')[0] == 'student_portal':
        return redirect(url_for('index'))
    else:
        return redirect(prev_route)

@app.route('/student_portal/enlistment', methods=['POST', 'GET'])
def enlistment():
    if request.method == 'POST' and request.referrer.endswith(url_for('enlistment')) and request.form['section_id'] != '-':
        courses_enlisted_in = Student.query.get(session['username']).courses_enlisted_in
        del courses_enlisted_in[request.form['course_code']]
        Student.query.get(session['username']).courses_enlisted_in = courses_enlisted_in

        free_slots = Section.query.get((request.form['course_code'], request.form['section_id'])).free_slots
        Section.query.get((request.form['course_code'], request.form['section_id'])).free_slots = free_slots + 1

        db.session.commit()

    elif request.method == 'POST' and request.referrer.endswith(url_for('enlist_in_section')):
        if request.form['course_code'] in Student.query.get(session['username']).courses_enlisted_in:
            free_slots = Section.query.get((request.form['course_code'], request.form['section_id'])).free_slots
            Section.query.get((request.form['course_code'], request.form['section_id'])).free_slots = free_slots + 1

            db.session.commit()

        # print(f"{Student.query.get(session['username']).courses_enlisted_in}")
        # print(request.form['course_code'])
        # print(request.form['section_id'])
        courses_enlisted_in = Student.query.get(session['username']).courses_enlisted_in
        courses_enlisted_in[request.form['course_code']] = request.form['section_id']
        Student.query.get(session['username']).courses_enlisted_in = courses_enlisted_in
        # Student.query.get(session['username']).courses_enlisted_in[request.form['course_code']] = request.form['section_id']
        # print(f"{Student.query.get(session['username']).courses_enlisted_in}")
        free_slots = Section.query.get((request.form['course_code'], request.form['section_id'])).free_slots
        Section.query.get((request.form['course_code'], request.form['section_id'])).free_slots = free_slots - 1

        db.session.commit()

        # return f"{Student.query.get(session['username']).courses_enlisted_in}"

    courses_to_enlist_in = Student.query.filter_by(id=session['username']).first().courses_to_enlist_in
    courses_enlisted_in = Student.query.filter_by(id=session['username']).first().courses_enlisted_in

    enlistment_data = [
        {
            'course_code': course_code,
            'section_id': courses_enlisted_in.get(course_code, '-'),
            'course_title': Course.query.get(course_code).title,
            'instructor': '-' if course_code not in courses_enlisted_in else Section.query.get((course_code, courses_enlisted_in[course_code])).instructor,
            'time': '-' if course_code not in courses_enlisted_in else Section.query.get((course_code, courses_enlisted_in[course_code])).time
        }
        for course_code in courses_to_enlist_in
    ]

    return render_template('EnlistmentPage.html', enlistment_data=enlistment_data)

@app.route('/student_portal/enlist_in_section', methods=['POST'])
def enlist_in_section():

    section_data = [
        {
            'course_code': section.course_code,
            'section_id': section.section_id,
            'course_title': Course.query.get(section.course_code).title,
            'units': Course.query.get(section.course_code).units,
            'time': section.time,
            'room': section.room,
            'instructor': section.instructor,
            'max_no': section.max_slots,
            'language': section.language,
            'level': Course.query.get(section.course_code).level,
            'free_slots': section.free_slots,
            'remarks': section.remarks,
            
        }
        for section in Course.query.get(request.form['course_code']).sections
    ]

    return render_template('EnlistmentSectionsPage.html', section_data=section_data)

@app.route('/student_portal/enrolled_classes')
def enrolled_classes():
    return render_template('MyCurrentlyEnrolledClassesPage.html')

@app.route('/student_portal/update_student_info', methods=['POST', 'GET'])
def update_student_info():
    if request.method == 'POST':
        for k, v in request.form.items():
            setattr(Student.query.filter_by(id = session['username']).first(), k, v)
            db.session.commit()
    return render_template('UpdateStudentInfo.html', student_info=Student.query.filter_by(id=session['username']).first())

@app.route('/student_portal/change_password', methods=['POST', 'GET'])
def change_password():
    if request.method == 'POST':
        if request.form['old_password'] == Student.query.filter_by(id=session['username']).first().password and \
        request.form['new_password'] == request.form['new_password_repeated']:
            Student.query.filter_by(id=session['username']).first().password = request.form['new_password']
            db.session.commit()
    return render_template('ChangePassword.html')

admin = Admin(app, name='microblog', template_mode='bootstrap3')

admin.add_view(ModelView(Announcement, db.session))
admin.add_view(ModelView(FAQ, db.session))
admin.add_view(ModelView(FaqCategory, db.session))
admin.add_view(ModelView(EnlistmentUpdate, db.session))
admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(Section, db.session))

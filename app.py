from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    session
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EmailType, PhoneNumberType, PasswordType
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
    Student
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

@app.route('/student_portal/enlistment')
def enrolled_classes():
    return render_template('EnlistmentPage.html')

@app.route('/student_portal/enrolled_classes')
def enlistment():
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

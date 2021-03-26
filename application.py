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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.jinja_env.add_extension('jinja2.ext.do')
db = SQLAlchemy(app)

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"post {self.id}\n \
            {self.title}\n \
            {self.date}\n  \
            {self.body}"

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(120), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('faq_category.id'), nullable=False)
    category = db.relationship('FaqCategory', backref=db.backref('faqs', lazy=True))

    def __repr__(self):
        return f"faq_category {self.category_id}\n\
            faq {self.id}\n\
            {self.question}\n\
            {self.answer}"

class FaqCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"faq_category {self.id}\n{self.name}"

class EnlistmentUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    prompt = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"enlistment_update {self.id}\n\
            faq {self.title}\n\
            {self.prompt}"

class Student(db.Model):            
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    primary_mobile = db.Column(PhoneNumberType, nullable=False)
    secondary_email = db.Column(EmailType, nullable=False)

    guardians_unit_no = db.Column(db.Integer)
    guardians_building = db.Column(db.String(100))
    guardians_street_no= db.Column(db.Integer)
    guardians_street_name = db.Column(db.String(100))
    guardians_village_brgy_name = db.Column(db.String(100))
    guardians_municipality = db.Column(db.String(100))
    guardians_city = db.Column(db.String(100))
    guardians_zip_code = db.Column(db.Integer)
    guardians_province = db.Column(db.String(100))
    guardians_country = db.Column(db.String(100))
    fathers_name = db.Column(db.String(100))
    mothers_name = db.Column(db.String(100))
    guardians_email = db.Column(db.String(100))
    guardians_landline = db.Column(PhoneNumberType)
    guardians_mobile_number = db.Column(PhoneNumberType)

    current_unit_no = db.Column(db.Integer)
    current_building = db.Column(db.String(100))
    current_street_no= db.Column(db.Integer)
    current_street_name = db.Column(db.String(100))
    current_village_brgy_name = db.Column(db.String(100))
    current_municipality = db.Column(db.String(100))
    current_city = db.Column(db.String(100))
    current_zip_code = db.Column(db.Integer)
    current_province = db.Column(db.String(100))
    current_country = db.Column(db.String(100))
    current_email = db.Column(db.String(100))
    current_landline = db.Column(PhoneNumberType)
    current_mobile_number = db.Column(PhoneNumberType)

    weekend_unit_no = db.Column(db.Integer)
    weekend_building = db.Column(db.String(100))
    weekend_street_no= db.Column(db.Integer)
    weekend_street_name = db.Column(db.String(100))
    weekend_village_brgy_name = db.Column(db.String(100))
    weekend_municipality = db.Column(db.String(100))
    weekend_city = db.Column(db.String(100))
    weekend_zip_code = db.Column(db.Integer)
    weekend_province = db.Column(db.String(100))
    weekend_country = db.Column(db.String(100))
    weekend_email = db.Column(db.String(100))
    weekend_landline = db.Column(PhoneNumberType)
    weekend_mobile_number = db.Column(PhoneNumberType)

    emergency_unit_no = db.Column(db.Integer)
    emergency_building = db.Column(db.String(100))
    emergency_street_no= db.Column(db.Integer)
    emergency_street_name = db.Column(db.String(100))
    emergency_village_brgy_name = db.Column(db.String(100))
    emergency_municipality = db.Column(db.String(100))
    emergency_city = db.Column(db.String(100))
    emergency_zip_code = db.Column(db.Integer)
    emergency_province = db.Column(db.String(100))
    emergency_country = db.Column(db.String(100))
    emergency_email = db.Column(db.String(100))
    emergency_landline = db.Column(PhoneNumberType)
    emergency_mobile_number = db.Column(PhoneNumberType)

    fathers_unit_no = db.Column(db.Integer)
    fathers_building = db.Column(db.String(100))
    fathers_street_no= db.Column(db.Integer)
    fathers_street_name = db.Column(db.String(100))
    fathers_village_brgy_name = db.Column(db.String(100))
    fathers_municipality = db.Column(db.String(100))
    fathers_city = db.Column(db.String(100))
    fathers_zip_code = db.Column(db.Integer)
    fathers_province = db.Column(db.String(100))
    fathers_country = db.Column(db.String(100))
    fathers_contact_person = db.Column(db.String(100))
    fathers_email = db.Column(db.String(100))
    fathers_landline = db.Column(PhoneNumberType)
    fathers_mobile_number = db.Column(PhoneNumberType)

    mothers_unit_no = db.Column(db.Integer)
    mothers_building = db.Column(db.String(100))
    mothers_street_no= db.Column(db.Integer)
    mothers_street_name = db.Column(db.String(100))
    mothers_village_brgy_name = db.Column(db.String(100))
    mothers_municipality = db.Column(db.String(100))
    mothers_city = db.Column(db.String(100))
    mothers_zip_code = db.Column(db.Integer)
    mothers_province = db.Column(db.String(100))
    mothers_country = db.Column(db.String(100))
    mothers_email = db.Column(db.String(100))
    mothers_landline = db.Column(PhoneNumberType)
    mothers_mobile_number = db.Column(PhoneNumberType)

    def __repr__(self):
        return f'<{self.id}, {self.password}>'

faqs = {category.name: FAQ.query.filter(FAQ.category_id==category.id) for category in FaqCategory.query.all()}

@app.route('/')
def index():
    # print('LOOKIE HERE', type(Announcement.query.all()))
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
    return render_template('FAQPage.html', faqs=faqs)

@app.route('/student_portal')
def student_portal():
    return render_template('StudentPortalPage.html')               

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

@app.route('/student_portal/update_student_info')
def update_student_info():
    return render_template('UpdateStudentInfo.html', student_info=Student.query.filter_by(id=session['username']).first())

@app.route('/student_portal/change_password')
def change_password():
    return render_template('ChangePassword.html')

admin = Admin(app, name='microblog', template_mode='bootstrap3')

admin.add_view(ModelView(Announcement, db.session))
admin.add_view(ModelView(Student, db.session))

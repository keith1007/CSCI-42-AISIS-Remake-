from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    session
)
from flask_sqlalchemy import SQLAlchemy


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
    if request.form['username'] == 'foo' and \
    request.form['password'] == 'bar':
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
    return render_template('UpdateStudentInfo.html')

@app.route('/student_portal/change_password')
def change_password():
    return render_template('ChangePassword.html')

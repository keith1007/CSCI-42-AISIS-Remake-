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
    return render_template('EnlistmentUpdatesPage.html')

@app.route('/faq')
def faq():
    return render_template('FAQPage.html')

@app.route('/student_portal')
def student_portal():
    return render_template('StudentPortalPage.html')               

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] == 'foo' and \
    request.form['password'] == 'bar':
        session['username'] = request.form['username']
    if 'username' in session:
        return redirect(url_for('student_portal'))
    else:
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

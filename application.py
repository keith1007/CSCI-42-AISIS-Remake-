from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    session
)


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return redirect(url_for('announcements'))

@app.route('/announcements')
def announcements():
    return render_template('AnnouncementsPage.html')

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
    prev_route = request.referrer.split('/')[-1]
    if 'username' in session:
        session.pop('username')
    if prev_route == 'student_portal':
        return redirect(url_for('announcements'))
    else:
        return redirect(url_for(prev_route))


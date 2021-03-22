from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


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

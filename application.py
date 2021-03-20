from flask import Flask, render_template


app = Flask(__name__)


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

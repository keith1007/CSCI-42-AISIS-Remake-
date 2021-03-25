from datetime import date
from application import (
    db,
    Announcement,
    FaqCategory,
    FAQ,
    EnlistmentUpdate
)

db.create_all()

Announcement.query.delete()
FaqCategory.query.delete()
FAQ.query.delete()
EnlistmentUpdate.query.delete()

# FOR ANNOUNCEMENTS
db.session.add(
	Announcement(
		title='Deadline for Submission by Undergraduate Students of Applications for Double Degree, effective SY 2021-2022',
		date=date(2021, 2, 22),
		body='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
	)
)

db.session.add(
	Announcement(
		title='Official Enrollment and Completion of Registration Process for Second Semester, School Year 2020-2021',
		date=date(2021, 2, 7),
		body='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
	)
)

db.session.add(
	Announcement(
		title='Adjustments to Academic Processes',
		date=date(2021, 1, 16),
		body='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
	)
)

db.session.add(
	Announcement(
		title='Adjusted Academic Calendar for the Second Semester, School Year 2020-2021',
		date=date(2020, 12, 2),
		body='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
	)
)

db.session.add(
	Announcement(
		title='Adjusted Academic Calendar for the remainder of the First Semester, School Year 2020-2021',
		date=date(2021, 11, 24),
		body='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
	)
)

db.session.add(
	Announcement(
		title='Requests for Reinstatement and/or Extension for Second Semester of School Year 2020-2021',
		date=date(2021, 10, 29),
		body='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
	)
)

# FOR FAQ RELATED DATA
faq_cat_getting_started = FaqCategory(name="Getting Started")
db.session.add(faq_cat_getting_started)

faq_cat_online_enlistment = FaqCategory(name="Online Enlistment")
db.session.add(faq_cat_online_enlistment)

faq_cat_online_assessment = FaqCategory(name="Online Assessment")
db.session.add(faq_cat_online_assessment)

faq_cat_payment = FaqCategory(name="Payment")
db.session.add(faq_cat_payment)

faq_cat_other_links = FaqCategory(name="Other Links")
db.session.add(faq_cat_other_links)

dummy_message = "We don't know the actual answer to this 😅"

db.session.add(
    FAQ(
        question="Charting a Re-imagined Path: Adaptive Teaching and Learning in the Loyola Schools 2020-2021",
        answer=dummy_message,
        category=faq_cat_getting_started
    )
)

db.session.add(
    FAQ(
        question="Code of Academic Integrity",
        answer=dummy_message,
        category=faq_cat_getting_started
    )
)

db.session.add(
    FAQ(
        question="Undergraduate Student Handbook 2018 Edition",
        answer=dummy_message,
        category=faq_cat_getting_started
    )
)

db.session.add(
    FAQ(
        question="AISIS Online FAQs",
        answer=dummy_message,
        category=faq_cat_getting_started
    )
)

db.session.add(
    FAQ(
        question="How to Enlist Online",
        answer=dummy_message,
        category=faq_cat_online_enlistment
    )
)

db.session.add(
    FAQ(
        question="Loyola Schools Directory",
        answer=dummy_message,
        category=faq_cat_online_enlistment
    )
)

db.session.add(
    FAQ(
        question="RegCom: Procedures, Batching Schedule, & FAQs",
        answer=dummy_message,
        category=faq_cat_online_enlistment
    )
)

db.session.add(
    FAQ(
        question="Online Enlistment Guidelines",
        answer=dummy_message,
        category=faq_cat_online_enlistment
    )
)

db.session.add(
    FAQ(
        question="Print your Assessment Forms at Home",
        answer=dummy_message,
        category=faq_cat_online_assessment
    )
)

db.session.add(
    FAQ(
        question="Tuition Payment Options for Interssion SY 2020-2021",
        answer=dummy_message,
        category=faq_cat_payment
    )
)

db.session.add(
    FAQ(
        question="Moodle",
        answer=dummy_message,
        category=faq_cat_other_links
    )
)

db.session.add(
    FAQ(
        question="Ateneo Website",
        answer=dummy_message,
        category=faq_cat_other_links
    )
)

# FOR ENLISTMENT UPDATES
db.session.add(
    EnlistmentUpdate(
        title="List of Interdisciplinary Electives (IE) Course Offerings for First Semester SY 2020-2021",
        date=date(2020, 8, 24),
        prompt="PDF File",
        content=dummy_message
    )
)

db.session.add(
    EnlistmentUpdate(
        title="Registration Schedule and Start of Classes for the First Semester, School Year 2020-2021",
        date=date(2020, 8, 20),
        prompt="Click here to view the memo",
        content=dummy_message
    )
)

# commit
db.session.commit()

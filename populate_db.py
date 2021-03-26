from datetime import date
from application import (
    db,
    Announcement,
    FaqCategory,
    FAQ,
    EnlistmentUpdate,
    Student
)
from flask_sqlalchemy import SQLAlchemy

db.drop_all()

db.create_all()

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

# FOR STUDENT INFO
db.session.add(
    Student(
        id = 420699,
        name = 'Rick Astley',
        year = 2,
        is_regular = True,
        degree = 'BS Management',
        password = '1234password',
        primary_mobile = '09999999999',
        secondary_email = 'dude@obf.ateneo.edu',
        guardians_unit_no = 1234,
        guardians_building = 'Somebuilding',
        guardians_street_no= 56,
        guardians_street_name = 'Stephen Nevada',
        guardians_village_brgy_name = 'Donut',
        guardians_municipality = 'NA',
        guardians_city = 'Kidzone City',
        guardians_zip_code = 7890,
        guardians_province = 'Albye',
        guardians_country = 'Philppines',
        fathers_name = 'Joe Mama',
        mothers_name = 'Joes Mama',
        guardians_email = 'joemama@rickroll.com',
        guardians_landline = '0521231234',
        guardians_mobile_number = '09999999999'
       )
)

db.session.add(
    Student(
        id = 000000,
        name = 'Shrekit Ralph',
        year = 4,
        is_regular = False,
        degree = 'BFA Information Design',
        password = 'foo',
        primary_mobile = '09999999991',
        secondary_email = 'dood@obf.ateneo.edu',
        guardians_unit_no = 1234,
        guardians_building = 'Somebuilding',
        guardians_street_no= 56,
        guardians_street_name = 'Stephen Nevada',
        guardians_village_brgy_name = 'Donut',
        guardians_municipality = 'NA',
        guardians_city = 'Kidzone City',
        guardians_zip_code = 7890,
        guardians_province = 'Albye',
        guardians_country = 'Philppines',
        fathers_name = 'Joe Mama',
        mothers_name = 'Joes Mama',
        guardians_email = 'joemama@rickroll.com',
        guardians_landline = '0521231234',
        guardians_mobile_number = '09999999999'
       )
)
# commit
db.session.commit()

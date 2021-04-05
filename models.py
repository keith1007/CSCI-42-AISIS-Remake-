from app import db
from sqlalchemy_utils import EmailType, PhoneNumberType, PasswordType


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"""post {self.id}
        {self.title}
        {self.date}
        {self.body}"""

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(120), nullable=False)
    answer = db.Column(db.Text, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('faq_category.id'), nullable=False)
    category = db.relationship('FaqCategory', backref=db.backref('faqs', lazy=True))

    def __repr__(self):
        return f"""faq_category {self.category_id}
        faq {self.id}
        {self.question}
        {self.answer}"""

class FaqCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"""faq_category {self.id}
        {self.name}"""

class EnlistmentUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    prompt = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"""enlistment_update {self.id}
        faq {self.title}
        {self.prompt}"""

class Student(db.Model):            
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    is_regular = db.Column(db.Boolean, nullable=False)
    degree = db.Column(db.String(100), nullable=False)
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
        return f'{self.id}'

class Course(db.Model):
    code = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    units = db.Column(db.Integer)
    level = db.Column(db.String(1))

    def __repr__(self):
        return f'{self.code}: {self.title}'


class Section(db.Model):
    course_code = db.Column(db.String(10), db.ForeignKey('course.code'), primary_key=True)
    section_id = db.Column(db.String(10), primary_key=True)
    time = db.Column(db.String(20), nullable=False)
    room = db.Column(db.String(20), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    max_slots = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(3), nullable=False)
    free_slots = db.Column(db.Integer, nullable=False)
    remarks = db.Column(db.String(100), nullable=False)

    course = db.relationship('Course', backref=db.backref('sections', lazy=True))

    def __repr__(self):
        return f'{self.code_code} {self.section_id}'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:password@localhost:3306/flamez', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String)
    mail_adress = Column(String)
    phone_number = Column(String)
    phone_number_mobile = Column(String)
    gender = Column(String)
    adress_id = Column(Integer, ForeignKey('adress.id'))
    item_id = Column(Integer)
    enrollment_id = Column(Integer, ForeignKey('enrollments.id'))

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', mail_adress='%s', phone_number='%s', phone_number_mobile='%s', gender='%s')>" % (self.first_name, self.last_name, self.mail_adress, self.phone_number, self.phone_number_mobile, self.gender)


class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String)
    typ = Column(String)
    status = Column(String)
    location = Column(String)
    price = Column(String)

    def __repr__(self):
        return "<Item(name='%s', typ='%s', status='%s', location='%s', price='%s')>" % (self.name, self.typ, self.status, self.location, self.price)


class Adress(Base):
    __tablename__ = 'adress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    street_name = Column(String)
    street_number = Column(Integer)
    street_number_suffix = Column(String)
    typ = Column(String)
    city = Column(String)
    postcode = Column(String)

    def __repr__(self):
        return "<Adress(street_name='%s', street_number='%s', street_number_suffix='%s', typ='%s', city='%s', postcode='%s')>" % (self.street_name, self.street_number, self.street_number_suffix, self.typ, self.city, self.postcode)


class Enrollments(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    date = Column(String)

    def __repr__(self):
        return "<Enrollments(date='%s')>" % (self.date)


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(Integer)
    approved = Column(String)
    description = Column(String)

    def __repr__(self):
        return "<Course(name='%s', location='%s', approved='%s', description='%s')>" % (self.name, self.location, self.approved, self.description)

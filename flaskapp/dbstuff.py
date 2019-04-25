"""
### Database File ###
- Contains the base for the connection & communication to the database 
- Defines all Database Tables 
- SQLAlchemy is an Object Relational Mapper which alows you too write Python Objects to talk to the Database instead of SQL Querys
"""

# importing sqlalchemy Modules to establish below(>>here is below<<) described processes
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# importing datatypes
from sqlalchemy import Column, Integer, String
# used to define a ForeignKey in my tables
from sqlalchemy import ForeignKey



# >>here is below<< (all of the following)
# represents the core interface to the database, MySQL dialect will interpret instructions to the Python built-in pymysql module
# echo flag is a shortcut to setting up SQLAlchemy logging (prints executed SQL Querys in the console)
engine = create_engine('mysql+pymysql://root:password@localhost:3306/flamez', echo=True)

# declarative_base is used to declare own classes for the database tables, its stored as Base (declarative base class)
Base = declarative_base()  # now its ready to define any number of mapped classes in terms of it

# this is the ORM “handle” which now can start talking to the databse
# it is used in the flaskapp.py to establish a connection and communication with the database
Session = sessionmaker(bind=engine)
# Session is associated with the Engine, but it hasn’t opened any connections yet.
# When it’s first used, it retrieves a connection from a pool of connections maintained by the Engine
# It holds onto it until all changes are commited and/or the session object is being closed.
session = Session()
# so when I know call .connect(), the Engine establishes a DBAPI connection to the database, which is then used to send/execute(emit) the SQL


# the following defined classes follow the same principle and are equal for all following classes
"""
1. Class object is defined and mapped to base
    - name is the same as the Database Table Name
    - the class is mapped to the base(which once again allows to write my own classes, like done below)
2. The Name of the Database Table is defined
3. Table Columns are defined
    - they are given the same name as in the databse
    - their Datatype is defined next
4. def __repr__(self)
    -  implement so that the classes show nicely formatted User objects.
    - returns the columns as the same name as in the table

"""


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

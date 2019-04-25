"""
### FORMS File ###
- contains all forms used in the application
- Files are created out of Python classes using flask_wtf/ wtforms
- there is no template/HTML File need because it is a function which is called and then being displayed
"""

# importing Modules
from flask_wtf import FlaskForm
# StringField(creates simple Text Input Field)
# RadioField(creates Radio Field)
# SubmitField(creates a Submit button)
from wtforms import StringField, SubmitField, RadioField
# imports validators which I am using to validate if the user did put in valid values
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional


# the following classes follow the same principles
"""
1. Class object is defined it refers to FlaskForms, can also be diffrent
2. The Name of the Form is defined
3. The type of the Form is defined
    - imported from wtforms, there is a StringField, SubmitField and RadioField available here
    - their Label(What the User sees) is defined next
    - next validators are defined, they can be Optional() or DataRequired() + an optional Lenght of the Input
"""


class SearchInventory(FlaskForm):
  name = StringField('Item Name',
                     validators=[Optional(), Length(min=2, max=20)])
  typ = StringField('Item Type',
                    validators=[Optional(), Length(min=2, max=20)])
  status = RadioField('Status', choices=[('In Storage', 'In Storage'), ('In Repair', 'In Repair'), ('Rent Out', 'Rent Out')])
  location = StringField('Location',
                         validators=[Optional(), Length(min=2, max=20)])
  price = StringField('Price',
                      validators=[Optional(), Length(min=2, max=20)])
  submit = SubmitField('Search Item')


class NewContactForm(FlaskForm):
  first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
  last_name = StringField('Last Name',
                          validators=[DataRequired(), Length(min=2, max=20)])
  mail_adress = StringField('Email',
                            validators=[DataRequired(), Email()])
  phone_number = StringField('Phone Number',
                             validators=[DataRequired(), Length(min=2, max=20)])
  phone_number_mobile = StringField('Phone Number Mobile',
                                    validators=[DataRequired(), Length(min=2, max=20)])
  gender = RadioField('Gender', choices=[('Female', 'Female'), ('Male', 'Male'), ('Divers', 'Divers')], validators=[DataRequired()])
  submit = SubmitField('Save Contact')


class NewItemForm(FlaskForm):
  name = StringField('Item Name',
                     validators=[DataRequired(), Length(min=2, max=20)])
  typ = StringField('Item Type',
                    validators=[DataRequired(), Length(min=2, max=20)])
  status = RadioField('Status', choices=[('In Storage', 'In Storage'), ('In Repair', 'In Repair'), ('Rent Out', 'Rent Out')])
  location = StringField('Location',
                         validators=[DataRequired(), Length(min=2, max=20)])
  price = StringField('Price',
                      validators=[DataRequired(), Length(min=2, max=20)])
  submit = SubmitField('Save Item')


class SearchContacts(FlaskForm):
  first_name = StringField('First Name',
                           validators=[Optional(), Length(min=2, max=20)])
  last_name = StringField('Last Name',
                          validators=[Optional(), Length(min=2, max=20)])
  mail_adress = StringField('Email',
                            validators=[Optional(), Email()])
  phone_number = StringField('Phone Number',
                             validators=[Optional(), Length(min=2, max=20)])
  phone_number_mobile = StringField('Phone Number Mobile',
                                    validators=[Optional(), Length(min=2, max=20)])
  gender = RadioField('Gender', choices=[('Female', 'Female'), ('Male', 'Male'), ('Divers', 'Divers')], validators=[Optional()])
  submit = SubmitField('Search Contact')


class ContactsUpdate(FlaskForm):
  first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
  last_name = StringField('Last Name',
                          validators=[DataRequired(), Length(min=2, max=20)])
  mail_adress = StringField('Email',
                            validators=[DataRequired(), Email()])
  phone_number = StringField('Phone Number',
                             validators=[DataRequired(), Length(min=2, max=20)])
  phone_number_mobile = StringField('Phone Number Mobile',
                                    validators=[DataRequired(), Length(min=2, max=20)])
  gender = RadioField('Gender', choices=[('Female', 'Female'), ('Male', 'Male'), ('Divers', 'Divers')], validators=[DataRequired()])
  submit = SubmitField('Save Contact')


class InventoryUpdate(FlaskForm):
  name = StringField('Item Name',
                     validators=[DataRequired(), Length(min=2, max=20)])
  typ = StringField('Item Type',
                    validators=[DataRequired(), Length(min=2, max=20)])
  status = RadioField('Status', choices=[('In Storage', 'In Storage'), ('In Repair', 'In Repair'), ('Rent Out', 'Rent Out')])
  location = StringField('Location',
                         validators=[DataRequired(), Length(min=2, max=20)])
  price = StringField('Price',
                      validators=[DataRequired(), Length(min=2, max=20)])
  submit = SubmitField('Save Item')

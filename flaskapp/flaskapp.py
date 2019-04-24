from flask import Flask, render_template, request, flash, redirect, url_for
from forms import NewContactForm, NewItemForm
from dbstuff import *


app = Flask(__name__)

app.config['SECRET_KEY'] = '77hf2HQeW789tccnt278t!t85cv8296t?8'


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    contacts = session.query(User).order_by(User.id).all()
    return render_template('contacts.html', contacts=contacts)


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    inventory = session.query(Item).order_by(Item.id).all()
    return render_template('inventory.html', inventory=inventory)


@app.route('/create_new_contact', methods=['GET', 'POST'])
def create_new_contact():
    form = NewContactForm()
    # if form.validate_on_submit():
    #     # user = User(first_name=forms.first_name.items(), last_name=forms.last_name.items(), mail_adress=forms.mail_adress.items(), phone_number=forms.phone_number.items(), phone_number_mobile=forms.phone_number_mobile.items(), gender=forms.gender.items())
    #     # session.add(user)
    #     # session.commit()
    #     # flash(f'User has been created.', 'success')
    #     # return redirect(url_for('contacts'))
    return render_template('create_new_contact.html', form=form)


@app.route('/create_new_item', methods=['GET', 'POST'])
def create_new_item():
    form = NewItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, typ=form.typ.data, status=form.status.data, location=form.location.data, price=form.price.data)
        session.add(item)
        session.commit()
        flash(f'Item has been created.', 'success')
        return redirect(url_for('inventory'))
    return render_template('create_new_item.html', form=form)

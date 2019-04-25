from flask import Flask, render_template, request, flash, redirect, url_for
from forms import NewContactForm, NewItemForm, SearchInventory, SearchContacts
from dbstuff import *


app = Flask(__name__)

app.config['SECRET_KEY'] = '77hf2HQeW789tccnt278t!t85cv8296t?8'


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    lenght_items = session.query(Item).count()
    lenght_contacts = session.query(User).count()
    return render_template('home.html',
                           lenght_contacts=lenght_contacts,
                           lenght_items=lenght_items)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():

    if request.method == "POST":
        contact_id = request.form["id"]
        delete = session.query(User).filter(
            User.id == contact_id).delete()
        session.commit()
        contacts = session.query(User).order_by(User.id).all()
        return render_template('contacts.html', contacts=contacts)

    contacts = session.query(User).order_by(User.id).all()
    return render_template('contacts.html', contacts=contacts)


@app.route('/search_contacts', methods=['GET', 'POST'])
def search_contacts():

    form = SearchContacts()

    if request.method == "POST":
        for users in session.query(User).filter(
                User.first_name == request.form["first_name"]):
            return render_template('search_contacts.html',
                                   form=form, users=users)

        for users in session.query(User).filter(
                User.last_name == request.form["last_name"]):
            return render_template('search_contacts.html',
                                   form=form, users=users)

        for users in session.query(User).filter(
                User.mail_adress == request.form["mail_adress"]):
            return render_template('search_contacts.html',
                                   form=form, users=users)

        for users in session.query(User).filter(
                User.phone_number == request.form["phone_number"]):
            return render_template('search_contacts.html',
                                   form=form, users=users)

        for users in session.query(User).filter(
                User.phone_number_mobile ==
                request.form["phone_number_mobile"]):
            return render_template('search_contacts.html',
                                   form=form, users=users)

    return render_template('search_contacts.html', form=form)


@app.route('/create_new_contact', methods=['GET', 'POST'])
def create_new_contact():

    form = NewContactForm()

    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    mail_adress=form.mail_adress.data,
                    phone_number=form.phone_number.data,
                    phone_number_mobile=form.phone_number_mobile.data,
                    gender=form.gender.data)

        session.add(user)
        session.commit()

        flash(f'User has been created.', 'success')
        return redirect(url_for('contacts'))

    return render_template('create_new_contact.html', form=form)


@app.route('/delete_contact', methods=['GET', 'POST'])
def delete_contact():
    return render_template('delete_contact.html')


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():

    if request.method == "POST":
        item_id = request.form["id"]
        delete = session.query(Item).filter(
            Item.id == item_id).delete()
        session.commit()
        inventory = session.query(Item).order_by(Item.id).all()
        return render_template('inventory.html',
                               inventory=inventory)

    inventory = session.query(Item).order_by(Item.id).all()
    return render_template('inventory.html',
                           inventory=inventory)


@app.route('/search_inventory', methods=['GET', 'POST'])
def search_inventory():

    form = SearchInventory()

    if request.method == "POST":
        for items in session.query(Item).filter(
                Item.name == request.form["name"]):
            return render_template('search_inventory.html',
                                   form=form, items=items)

        for items in session.query(Item).filter(
                Item.typ == request.form["typ"]):
            return render_template('search_inventory.html',
                                   form=form, items=items)

        for items in session.query(Item).filter(
                Item.location == request.form["location"]):
            return render_template('search_inventory.html',
                                   form=form, items=items)

        for items in session.query(Item).filter(
                Item.price == request.form["price"]):
            return render_template('search_inventory.html',
                                   form=form, items=items)

    return render_template('search_inventory.html', form=form)


@app.route('/create_new_item', methods=['GET', 'POST'])
def create_new_item():
    form = NewItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data,
                    typ=form.typ.data,
                    status=form.status.data,
                    location=form.location.data,
                    price=form.price.data)

        session.add(item)
        session.commit()

        flash(f'Item has been created.', 'success')
        return redirect(url_for('inventory'))

    return render_template('create_new_item.html', form=form)

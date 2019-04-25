"""
### FLASK_APP File ###
- This is the heart of the application (also often known as __init__.py)
- defines all URL / routes and what each route should do
- imports Modules externally(not written by me e.g. flask) and internally(written by me e.g. forms)

>> “Oh! Now we see the violence inherent in the system! Help, help, I’m being repressed!” <<   - Monty Python and the Holy Grail
"""

# here I import external/ inernal Modules. Why I use them?:

# render_template(for returning Templates),
# request(to get data from forms),
# flash(for flashing messages to the user),
# redirect(for redirecting to a choosen page)
# url_for(needed in combination with redirect to create a link)
from flask import Flask, render_template, request, flash, redirect, url_for
# importing ownwritten Forms from forms.py(self explained what they might be for)
from forms import NewContactForm, NewItemForm, SearchInventory, SearchContacts, InventoryUpdate, ContactsUpdate
# importing the database session I work with e.g. ->'session'<-.add() (detailed info in dbstuff.py)
from dbstuff import *


# creating an instance of the Flask class, stored in app
# __name__ is set equal to '__main__' which runs the app
# also needed so that Flask knows where to look for templates, static files, and so on
app = Flask(__name__)


# used for securely signing the session cookie and can be used for any other security related needs
# should not be shown/ know by some1 else
app.config['SECRET_KEY'] = '77hf2HQeW789tccnt278t!t85cv8296t?8'


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    >>> Index/Landing/Welcome Page <<<
    - displaying how many Contacts & Items the User has
    """

    # querying databse tables and fetching lenght of tables, stored in lenght_x
    lenght_items = session.query(Item).count()
    lenght_contacts = session.query(User).count()

    # rendering template, returning lenghts
    return render_template('home.html',
                           lenght_contacts=lenght_contacts,
                           lenght_items=lenght_items)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    """
    >>> Contact Page <<<
    - displaying all contacts
    - defining delete contact function
    """

    # Delete Button triggers POST method
    if request.method == "POST":
        # getting User ID from non displayed form and stores it in contact_id
        contact_id = request.form["id"]
        # defines delete querys with WHERE condition User ID
        delete = session.query(User).filter(
            User.id == contact_id).delete()
        # commit() flushes session and executes the delete
        session.commit()
        # getting all Contacts from User table
        contacts = session.query(User).order_by(User.id).all()
        # this return is triggered by the Delete(=="POST") Button
        return render_template('contacts.html', contacts=contacts)

    # getting all Contacts ordered by ID from User table
    contacts = session.query(User).order_by(User.id).all()
    # rendering template, returning contacts(all contacts)
    return render_template('contacts.html', contacts=contacts)


@app.route('/search_contacts', methods=['GET', 'POST'])
def search_contacts():
    """
    >>> Contact Page // Search Contacts Page <<<
    - imports Search Contact Form and displays it
    - defines search functions to query the Database Table 'User'
    """

    # importing Search Contact Form from forms.py, and stores it in form
    form = SearchContacts()

    # Search Button triggers POST method
    if request.method == "POST":
        # querys 'User' Table (WHERE Condition == User Input)
        # renders search_contacts Template
        # returns form and users(found users)
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
                User.phone_number_mobile == request.form["phone_number_mobile"]):
            return render_template('search_contacts.html',
                                   form=form, users=users)

    # rendering template, returning form
    return render_template('search_contacts.html', form=form)


@app.route('/create_new_contact', methods=['GET', 'POST'])
def create_new_contact():
    """
    >>> Contact Page // Create New Contact Page <<<
    - Displays a Form to create a new Contact
    - Gets the input and saves it in the Databse
    - Brings you back to the Contacts Page afterwards
    """

    # importing Search Item Form from forms.py, and stores it in form
    form = NewContactForm()

    # if Form Input is valid(filled out and valid)
    if form.validate_on_submit():
        # the data gets requested from the forms
        # next stored in a variable as their Database Column Name
        # everthing stored in user variable
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    mail_adress=form.mail_adress.data,
                    phone_number=form.phone_number.data,
                    phone_number_mobile=form.phone_number_mobile.data,
                    gender=form.gender.data)

        # user variable given to add() function
        # adds stored values to the session
        session.add(user)
        # session values are now commited to the Database Table 'User'
        session.commit()

        # and finally redirecting back to contacts.html
        return redirect(url_for('contacts'))

    # rendering template, returning form
    return render_template('create_new_contact.html', form=form)


@app.route('/contacts_update', methods=['GET', 'POST'])
def contacts_update():
    """
    >>> Contact Page // Contacts Update <<<
    - Updates Contact entry
    """

    # importing Contact Update Form from forms.py, and stores it in form
    form = ContactsUpdate()

    # if Form Input is valid(filled out and valid)
    if form.validate_on_submit():
        # the data gets requested from the forms
        # next stored in a variable as their Database Column Name
        # everthing stored in user variable
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    mail_adress=form.mail_adress.data,
                    phone_number=form.phone_number.data,
                    phone_number_mobile=form.phone_number_mobile.data,
                    gender=form.gender.data)

        # updated item given to add() function
        # adds stored values to the session
        session.add(user)
        # session values are now commited to the Database Table 'Item'
        session.commit()
        # rendering template, returning form and user
        return render_template('contacts.html', form=form, user=user)

    # rendering template, returning form
    return render_template('contacts_update.html', form=form)


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    """
    >>> Inventory Page<<<
    - displaying all Items
    - defining delete Item function
    """

    # Delete Button triggers POST method
    if request.method == "POST":
        # getting Item ID from non displayed form and stores it in item_id
        item_id = request.form["id"]
        # defines delete querys with WHERE condition Item ID
        delete = session.query(Item).filter(
            Item.id == item_id).delete()
        # commit() flushes session and executes the delete
        session.commit()
        # getting all Items from 'Item' table
        inventory = session.query(Item).order_by(Item.id).all()
        return render_template('inventory.html',
                               inventory=inventory)

    # getting all Items from 'Item' table
    inventory = session.query(Item).order_by(Item.id).all()
    # rendering template, returning inventory(all items)
    return render_template('inventory.html',
                           inventory=inventory)


@app.route('/search_inventory', methods=['GET', 'POST'])
def search_inventory():
    """
    >>> Inventory Page // Search Inventory Page <<<
    - imports Search Inventory Form and displays it
    - defines search functions to query the Database Table 'Item'
    """

    # importing Search Inventory Form from forms.py, and stores it in form
    form = SearchInventory()

    # Search Button triggers POST method
    if request.method == "POST":
        # querys 'Item' Table (WHERE Condition == User Input)
        # renders search_inventory Template
        # returns form and items(found items)
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

    # rendering template, returning form
    return render_template('search_inventory.html', form=form)


@app.route('/create_new_item', methods=['GET', 'POST'])
def create_new_item():
    """
    >>> Inventory Page // Create New Item Page <<<
    - Displays a Form to create a new Item
    - Gets the input and saves it in the Databse
    - Brings you back to the Inventory Page afterwards
    """

    # importing Create Item Form from forms.py, and stores it in form
    form = NewItemForm()

    # if Form Input is valid(filled out and valid) is True it runs the if clause
    if form.validate_on_submit():
        # the data gets requested from the forms
        # next stored in a variable as their Database Column Name
        # everthing stored in item variable
        item = Item(name=form.name.data,
                    typ=form.typ.data,
                    status=form.status.data,
                    location=form.location.data,
                    price=form.price.data)

        # user variable given to add() function
        # adds stored values to the session
        session.add(item)
        # session values are now commited to the Database Table 'User'
        session.commit()

        # displaying a success message
        flash(f'Item has been created.', 'success')
        # redirecting back to contacts.html
        return redirect(url_for('inventory'))

    # rendering template, returning form
    return render_template('create_new_item.html', form=form)


@app.route('/inventory_update', methods=['GET', 'POST'])
def inventory_update():
    """
    >>> Inventory Page // Inventory Update <<<
    - Updates Item entry
    """

    # importing Inventory Update Form from forms.py, and stores it in form
    form = InventoryUpdate()

    # if Form Input is valid(filled out and valid)
    if form.validate_on_submit():
        # the data gets requested from the forms
        # next stored in a variable as their Database Column Name
        # everthing stored in user variable
        item = Item(name=form.name.data,
                    typ=form.typ.data,
                    status=form.status.data,
                    location=form.location.data,
                    price=form.price.data)

        # updated item given to add() function
        # adds stored values to the session
        session.add(item)
        # session values are now commited to the Database Table 'Item'
        session.commit()
        # rendering template, returning form and item
        return render_template('inventory.html', form=form, item=item)

    # rendering template, returning form and item
    return render_template('inventory_update.html', form=form, item=item)

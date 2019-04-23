from flask import Flask, render_template, request
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "flamez")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    contacts = cursor.fetchall()
    lenght_contacts = len(contacts)
    cursor.execute("SELECT * FROM item")
    items = cursor.fetchall()
    lenght_items = len(items)
    cursor.close()
    db.close()
    return render_template('home.html', lenght_contacts=lenght_contacts, lenght_items=lenght_items)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():

    db = MySQLdb.connect("127.0.0.1", "root", "password", "flamez")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    contacts = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('contacts.html', contacts=contacts)


@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "flamez")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM item")
    items = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('inventory.html', items=items)


@app.route('/create_new_contact', methods=['GET', 'POST'])
def create_new_contact():
    return render_template('create_new_contact.html')


@app.route('/create_new_item', methods=['GET', 'POST'])
def create_new_item():
    return render_template('create_new_item.html')

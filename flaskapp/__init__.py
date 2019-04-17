from flask import Flask, render_template, request
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


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


@app.route('/create_new', methods=['GET', 'POST'])
def create_new():
    db = MySQLdb.connect("127.0.0.1", "root", "password", "flamez")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    user = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('create_new.html', user=user)

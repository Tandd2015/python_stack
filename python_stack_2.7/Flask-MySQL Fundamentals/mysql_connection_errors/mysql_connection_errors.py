from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection1 import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():

    print mysql.query_db("SELECT * FROM friendsdb.friends")
    return render_template('index.html')

app.run(debug=True)
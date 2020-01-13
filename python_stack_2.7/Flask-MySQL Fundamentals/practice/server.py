from flask import Flask
from mysqlconnection1 import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'sakila')

print mysql.query_db("SELECT * FROM actor")

app.run(debug=True)

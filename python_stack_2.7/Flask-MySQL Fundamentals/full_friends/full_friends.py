from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "WhataSecret!"
mysql = MySQLConnector(app, 'full_friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM full_friendsdb.friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_my_friends=friends)

@app.route('/add_friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM full_friendsdb.friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

@app.route('/add_friends', methods=['POST'])
def create():
    query = "INSERT INTO full_friendsdb.friends (friends.first_name, friends.last_name, friends.occupation, friends.created_at, friends.updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
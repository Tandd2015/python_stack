from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')


# @app.route('/')
# def index():
#     friends = mysql.query_db("SELECT * FROM friendsdb.friends")
#     print friends
#     return render_template('index.html')

# @app.route('/friends', methods=['POST'])
# def create():
#     return redirect('/')
# app.run(debug=True)


# @app.route('/')
# def index():
#     query = "SELECT * FROM friendsdb.friends"
#     friends = mysql.query_db(query)
#     return render_template('index.html', all_friends=friends)

# @app.route('/friends', methods=['POST'])
# def create():
#     return redirect('/')
# app.run(debug=True)


# @app.route('/')
# def index():
#     query = "SELECT * FROM friendsdb.friends"
#     friends = mysql.query_db(query)
#     return render_template('index.html', all_friends=friends)

# @app.route('/friends/<friend_id>')
# def show(friend_id):
    
#     query = "SELECT * FROM friendsdb.friends WHERE id = :specific_id"
#     data = {'specific_id': friend_id}
#     friends = mysql.query_db(query, data)
#     return render_template('index.html', one_friend=friends[0])

# @app.route('/friends', methods=['POST'])
# def create():
    
#     # print request.form['first_name']
#     # print request.form['last_name']
#     # print request.form['occupation']
#     return redirect('/')
# app.run(debug=True)


# @app.route('/')
# def index():
#     query = "SELECT * FROM friendsdb.friends"
#     friends = mysql.query_db(query)
#     return render_template('index.html', all_friends=friends)

# @app.route('/friends/<friend_id>')
# def show(friend_id):
    
#     query = "SELECT * FROM friendsdb.friends WHERE id = :specific_id"
#     data = {'specific_id': friend_id}
#     friends = mysql.query_db(query, data)
#     return render_template('index.html', one_friend=friends[0])

# @app.route('/friends', methods=['POST'])
# def create():

#     query = "INSERT INTO friendsdb.friends (friends.first_name, friends.last_name, friends.occupation, friends.created_at, friends.updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"

#     data = {
        
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'occupation': request.form['occupation']
#     }
#     mysql.query_db(query, data)
#     return redirect('/')
# app.run(debug=True)


# @app.route('/')
# def index():
#     query = "SELECT * FROM friendsdb.friends"
#     friends = mysql.query_db(query)
#     return render_template('index.html', all_friends=friends)

# @app.route('/friends/<friend_id>')
# def show(friend_id):
    
#     query = "SELECT * FROM friendsdb.friends WHERE id = :specific_id"
#     data = {'specific_id': friend_id}
#     friends = mysql.query_db(query, data)
#     return render_template('index.html', one_friend=friends[0])

# @app.route('/friends', methods=['POST'])
# def create():

#     query = "INSERT INTO friendsdb.friends (friends.first_name, friends.last_name, friends.occupation, friends.created_at, friends.updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"

#     data = {
        
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'occupation': request.form['occupation']
#     }
#     mysql.query_db(query, data)
#     return redirect('/')

# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
    
#     query = "UPDATE friendsdb.friends SET friends.first_name = :first_name, friends.last_name = :last_name, friends.occupation = :occupation WHERE friends.id :id"

#     data = {
        
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'occupation': request.form['occupation'],
#         'id': friend_id
#     }
#     mysql.query_db(query, data)
#     return redirect('/')
# app.run(debug=True)

@app.route('/')
def index():
    query = "SELECT * FROM friendsdb.friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends/<friend_id>')
def show(friend_id):
    
    query = "SELECT * FROM friendsdb.friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0])

@app.route('/friends', methods=['POST'])
def create():

    query = "INSERT INTO friendsdb.friends (friends.first_name, friends.last_name, friends.occupation, friends.created_at, friends.updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"

    data = {
        
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    
    query = "UPDATE friendsdb.friends SET friends.first_name = :first_name, friends.last_name = :last_name, friends.occupation = :occupation WHERE friends.id :id"

    data = {
        
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation'],
        'id': friend_id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    
    query = "DELETE FROM friendsdb.friends WHERE friends.id = :id"
    
    data = {'id': friend_id}

    mysql.query_db(query, data)
    return redirect('/')
    
app.run(debug=True)
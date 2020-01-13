# our_list = ['martin', 'michael']
# for val in enumerate(our_list):
#     print val

# counter_list = list(enumerate(our_list, 1))
# print(counter_list)

# for idx,value in enumerate(our_list):
#     print value, idx

# scott = {
#     "name":"Scott",
#     "lname":"Brown",
#     "age":"27",
#     "hobbies":["coding", "digital art", "art"]
# }
# key, value = "AP"
# print key, value

# name = {"sw":"Sara Wong", "mp":"Martin Puryear"}
# for key, value in name.items(): # every dictionary has a local items() function
#     print key, value

# my_people = [
#     {"name":"scott", "blackbelt":"pending"},
#     {"name":"ana", "blackbelt":"pending"},
#     {"name":"kyle", "blackbelt":"pending"},
#     {"name":"seth", "blackbelt":"pending"},
#     {"name":"anthony", "blackbelt":"pending"},
#     {"name":"Minh", "blackbelt":True},
# ]
# for i in my_people:
#     print i
#     if i["blackbelt"] == "pending":
#         print i["name"]




# this is a user being put into the database
import md5
# this is for generating salt //////
import os, binascii
@app.route('users/create', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username, :email, :password, NOW(), NOW())"
    query_data = {
        'username': username
        'email': email
        'password': password
    }
    mysql.query_db(insert_query, query_data)

# this is when a user is logging in 
@app.route('users/login', methods=['POST'])
def login_user():
    password1 = md5.new(request.form['password']).hexdigest()
    email1 = request.form['email']
    user_query1 = "SELECT * FROM users where users.email = :email1 AND users.password = :password1"
    query_data1 = {
        'email1': email1
        'password1': password1
    }
    user1 = mysql.query_db(user_query1, query_data1)
    #do the necessary logic to login if the user exist, otherwise redirect
    #to login page with error messages

salt = '123' #where the value 123 changes randomly
hashed_password = md5(password + salt)
# //////
salt = binascii.b2a_hex(os.urandom(15))

@app.route('users/create1', methods=['POST'])
def create_user1():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    salt = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()
    insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at) VALUES (:username, :email, :hashed_pw, :salt, NOW(), NOW())"
    query_data = {
        'username': username
        'email': email
        'hashed_pw': hashed_pw
        'salt': salt
    }
    mysql.query_db(insert_query, query_data)

@app.route('users/login1', methods=['POST'])
def login_user1():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {
        'email': email
    }
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password
        #this would be a successful login
        else:
        #flash that the password was invalid and unsuccessful login occurred
    else:
    #flash that the email was invalid and unsuccessful login occured
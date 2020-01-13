from flask import Flask, render_template, session, flash, redirect, request
from mysqlconnection import MySQLConnector
import datetime
import re
import md5
import os, binascii

EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
app = Flask(__name__)
app.secret_key = "IaMBaCk2019"
mysql = MySQLConnector(app, 'Log')

@app.route("/login_form")
@app.route("/registeration_form")
def charFinder(string):
    charfound = False
    if len(string) == 0:
        charfound = True
    else:    
        for index in string:
            if not index.isalpha():
                charfound = True
                break
            else:
                charfound = False
    return charfound

@app.route('/login_form')
def email_check(databases, input_field):
    check = False
    for index in databases:
        for key, data in index.iteritems():
            if input_field == data:
                check = True
                for key, data in index.iteritems():
                    if key == 'id':
                        session.pop('id_check')
                        session['id_check'] = data
                        break
    return check

@app.route('/login_form')
def id_n_check(dbs, inputs, inputs1):
    i_d_check = False
    for index in dbs:
        for key, data in index.iteritems():
            if inputs == data:
                for key, data in index.iteritems():
                    if inputs1 == data:
                        i_d_check = True
                        break
    return i_d_check

@app.route('/')
def LoadInfo():
    query = "SELECT * FROM Log.users"
    db = mysql.query_db(query)
    if 'db_copy' not in session:
        session['db_copy'] = db
    elif 'db_copy' in session and session['db_copy'] <> db:
        session.pop('db_copy')
        session['db_copy'] = db
    else:
        session['db_copy'] = session['db_copy']
    
    if 'logged_user' not in session:
        session['logged_user'] = None
    else:
        session['logged_user'] = session['logged_user']

    if 'id' not in session:
        session['id'] = None
    else:
        session['id'] = session['id']

    if 'message_class' not in session:
        session['message_class'] = "alert alert-danger"
    else:
        session.pop('message_class')
        session['message_class'] = "alert alert-danger"
    if 'id_check' not in session:
        session['id_check'] = None
    else:
        session['id_check'] = session['id_check']    

    if 'user32' not in session:
        session['user32'] = None
    else:
        session['user32'] = session['user32']
    return render_template('login.html')


@app.route("/login_form", methods=['POST'])
def Login_validation():
    password = request.form['login_password']
    email = request.form['login_email_address']
    query3 = "SELECT * FROM users WHERE users.email_address = :email LIMIT 1"
    data3 = {
        'email': email
    }
    user3 = mysql.query_db(query3, data3)
    login_counter = 0
    if len(user3) <> 0:
        if 'user32' not in session:
            session['user32'] = user3
        elif 'user32' in session and user3 <> session['user32']:
            session.pop('user32')
            session['user32'] = user3
        else:
            session['user32'] = session['user32']
        encrypted_password = md5.new(password + user3[0]['salt']).hexdigest()
    else:
        session.pop('user32')
        session['user32'] = None

    if len(request.form['login_email_address']) < 1:
        flash(u'Email Address field can not be blank', 'error')
    elif not EMAIL_REGEX.match(request.form['login_email_address']):
        flash(u'This is an invalid email address', 'error')
    elif EMAIL_REGEX.match(request.form['login_email_address']) and \
        email_check(session['db_copy'], request.form['login_email_address']) == False:
            flash(u'This email address is not a registered','error')
    else:
        login_counter += 1

    if len(request.form['login_password']) <= 7:
        flash(u'Password must be at least 8 characters length', 'error')
    elif len(request.form['login_password']) >= 7 and email_check(session['db_copy'], \
        request.form['login_email_address']) == True and session['user32'][0]['password'] <> encrypted_password:
            flash(u'Invalid Password is not users password', 'error') 
    else:
        login_counter += 1

    if len(request.form['login_f_name']) <= 1:
        flash(u'First name field must contain at least two letters', 'error')
    elif charFinder(request.form['login_f_name']) == True and \
        len(request.form['login_f_name']) >= 1:
            flash(u'First name field can only contain letters', 'error')
    elif charFinder(request.form['login_f_name']) == False and \
        len(request.form['login_f_name']) >= 1 and id_n_check(session['db_copy'], \
        request.form['login_f_name'], session['id_check']) == False:
            flash(u'First name entry did not match database information', 'error')
    else:
        login_counter += 1

    if len(request.form['login_l_name']) <= 1:
        flash(u'Last name field must contain at least two letters', 'error')
    elif charFinder(request.form['login_l_name']) == True and \
            len(request.form['login_l_name']) >= 1:
                flash(u'Last name field can only contain letters', 'error')
    elif charFinder(request.form['login_l_name']) == False and \
        len(request.form['login_l_name']) >= 1 and id_n_check(session['db_copy'], \
        request.form['login_l_name'], session['id_check']) == False:
            flash(u'Last name entry did not match database information', 'error')    
    else:
        login_counter += 1
    
    if login_counter == 4:
        if 'login_success' not in session:
            session['login_success'] = "You have successfully logged in"
        else:
            session.pop('login_success')
            session['login_success'] = "You have successfully logged in"            
        if 'register_success' not in session:
            session['register_success'] = None
        else:
            session.pop('register_success')
            session['register_success'] = None        
        session['logged_user'] = session['user32']
        session.pop('id')
        session['id'] = session['logged_user'][0]['id'] 
        session.pop('logged_user')
        session['logged_user'] = None
        session.pop('id_check')
        session['id_check'] = None
        return redirect('/success')
    # print session['logged_user']
    # print session['user32']
    # print user3
    # print login_counter
    # print session['db_copy']
    session.pop('id_check')
    session['id_check'] = None
    return redirect('/')

@app.route("/registeration_page")
def LoadRegisteration():
    if 'message_success' not in session:
        session['message_class'] = "alert alert-danger"
    else:
        session.pop('message_class')
        session['message_class'] = "alert alert-danger"

    if 'rid' not in session:
        session['rid'] = None
    else:
        session['rid'] = session['rid']
        
    if 'ruser11' not in session:
        session['ruser11'] = None
    else:
        session['ruser11'] = session['ruser11']
    return render_template('registeration.html')

@app.route("/registeration_form", methods=['POST'])
def Registeration_validation():
    registeration_counter = 0
    if len(request.form['registeration_email']) < 1:
        flash(u'Email Address field can not be blank', 'error')
    elif not EMAIL_REGEX.match(request.form['registeration_email']):
        flash(u'This is an invalid email address', 'error')
    else:
        registeration_counter += 1
    
    if len(request.form['registeration_f_name']) <= 1:
        flash(u'First name field must contain at least two letters', 'error')
    elif charFinder(request.form['registeration_f_name']) == True and len(request.form['registeration_f_name']) >= 1:
        flash(u'First name field can only contain letters', 'error')
    else:
        registeration_counter += 1

    if len(request.form['registeration_l_name']) <= 1:
        flash(u'Last name field must contain at least two letters', 'error')
    elif charFinder(request.form['registeration_l_name']) == True and len(request.form['registeration_l_name']) >= 1:
        flash(u'Last name field can only contain letters', 'error')
    else:
        registeration_counter += 1

    if len(request.form['registeration_password']) <= 7:
        flash(u'Password must be at least 8 characters length', 'error')
    elif len(request.form['registeration_password']) >= 7 and \
           request.form['registeration_password'] <>  \
           request.form['registeration_r_password']:
        flash(u'Password field does not match Re-Enter Password field', 'error') 
    else:
        registeration_counter += 1

    if len(request.form['registeration_r_password']) <= 7:
        flash(u'Re-Enter Password field must be at least 8 characters in length', 'error')
    elif len(request.form['registeration_r_password']) >= 7 and \
           request.form['registeration_r_password'] <>  \
           request.form['registeration_password']:
        flash(u'Re-Enter Password field does not match Password field', 'error') 
    else:
        registeration_counter += 1

    if registeration_counter == 5:
        if 'register_success' not in session:
            session['register_success'] = "You have successfully Registered"
        else:
            session.pop('register_success')
            session['register_success'] = "You have successfully Registered" 
        if 'login_success' not in session:
            session['login_success'] = None
        else:
            session.pop('login_success')
            session['login_success'] = None            
     
        emails = request.form['registeration_email']
        password = request.form['registeration_r_password']
        first = request.form['registeration_f_name']
        last = request.form['registeration_l_name']
        salt = binascii.b2a_hex(os.urandom(15))
        hashed_password = md5.new(password + salt).hexdigest()
        query = "INSERT INTO Log.users (users.email_address, users.password, users.salt, users.first_name, users.last_name, users.created_at, users.updated_at) VALUES (:email_address, :password, :salt, :first_name, :last_name, NOW(), NOW())"
        data = {
            'email_address': emails,
            'password': hashed_password,
            'salt': salt,
            'first_name': first,
            'last_name': last
        }
        mysql.query_db(query, data)

        query4 = "SELECT * FROM users WHERE users.email_address = :email LIMIT 1"
        data4 = {
            'email': emails
        }
        user4 = mysql.query_db(query4, data4)
        session.pop('rid')
        session['rid'] = user4[0]['id']

        return redirect('/success')
    # print registeration_counter
    # query1 = "SELECT * FROM Log.users"
    # d1 = mysql.query_db(query1)
    # print d1
    # print request.form
    return redirect('/registeration_page')

@app.route('/success')
def show_user():
    if 'ruser11' not in session:
        session['ruser11'] = None
    else:
        session['ruser11'] = session['ruser11']
    
    if 'user11' not in session:
        session['user11'] = None
    else:
        session['user11'] = session['user11']

    if 'id' in session and session['id'] <> None:
        session.pop('message_class')
        session['message_class'] = "alert alert-success"
        user_id = session['id']
        last_query = "SELECT * FROM Log.users WHERE id = :specific_id"
        final_data = {
            'specific_id': user_id
        }
        user1 = mysql.query_db(last_query, final_data)    
        
        if 'user_11' not in session:
            session['user11'] = user1
        else:
            session.pop('user11')
            session['user11'] = user1
        if 'login_success' in session and session['login_success'] <> None:
            flash(u'{}'.format(session['login_success']), 'success')
        session.pop('id', None)
        session.pop('rid',None)
        return render_template('success.html', user111 = session['user11'])
    elif 'rid' in session and session['rid'] <> None:
        session.pop('message_class')
        session['message_class'] = "alert alert-success"
        ruser_id = session['rid']
        last_queryy = "SELECT * FROM Log.users WHERE id = :specific_id"
        final_datar = {
            'specific_id': ruser_id
        }
        ruser1 = mysql.query_db(last_queryy, final_datar)    
        
        if 'ruser_11' not in session:
            session['ruser11'] = ruser1
        else:
            session.pop('ruser11')
            session['ruser11'] = ruser1
        
        if 'register_success' in session and session['register_success'] <> None:
            flash(u'{}'.format(session['register_success']), 'success')                   
    
        session.pop('id', None)
        session.pop('rid',None)
        return render_template('success.html', user1111 = session['ruser11'])
    else:
        session.pop('message_class')
        session['message_class'] = "alert alert-danger"
        flash(u'There was a problem while logging in, login failed', 'error')
    session.pop('id', None)
    session.pop('rid',None)
    return render_template('success.html')
app.run(debug=True)
from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
import datetime
import re

EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

app = Flask(__name__)
app.secret_key = "GettingBetter1!"
mysql = MySQLConnector(app, 'email_address_book_db')

@app.route('/')
def index():
    query = "SELECT * FROM email_address_book_db.email_addresses"
    db_email_address = mysql.query_db(query)

    if 'success_winner_message' not in session:
        session['class'] = "alert alert-danger"
    else:
        session.pop('class')
        session['class'] = "alert alert-success"
        session.pop('_flashes', None)
        flash(u'{}'.format(session['success_winner_message']), 'success')
        session.pop('success_winner_message')

    if 'db_email_addresses' not in session:
        session['db_email_addresses'] = db_email_address
        for session['email_addresses'] in session['db_email_addresses']:
            session['email_addresses'] = session['email_addresses']
    elif 'db_email_addresses' in session and session['db_email_addresses'] != db_email_address:
        session['email_addresses'] = db_email_address
    else:
        session['db_email_addresses'] = session['db_email_addresses']

    if 'count' not in session:
        session['count'] = 0
    elif session['count'] >= 1:
        session.pop('count')
        session['count'] = 0
        session['class'] = "alert alert-success"
        return redirect('/success')
    else:
        session['count'] = session['count']
    return render_template('index.html')

@app.route('/check_emails', methods=['POST'])
def validate_email():

    if 'email_count' not in session:
        session['email_count'] = 0
    else:
        session['email_count'] = session['email_count']

    if len(request.form['email_address']) < 1:
        flash(u'Email Address field can not be blank.', 'error')
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash(u'The Email Address is Invalid.', 'error')
    else:
        for session['email_addresses'] in session['db_email_addresses']:
            if session['email_addresses']['email_address'] == request.form['email_address']:
                session['count'] += 1
                session['winner_message'] = "The email address you entered {} is a valid email address!  Thank you!".format(request.form['email_address'])
                session.pop('email_count')
                session['email_count'] = 0
            else:
                session['email_count'] += 1
        if session['email_count'] > 0:
            flash(u'The Email Address does not exsist within the database', 'error')
            session.pop('email_count')
            session['email_count'] = 0

    return redirect('/')
        

@app.route('/success')
def success_index():
    query = "SELECT * FROM email_address_book_db.email_addresses"
    db_email_address = mysql.query_db(query)

    if 'success_db_email_addresses' not in session:
        session['success_db_email_addresses'] = db_email_address
        for session['success_email_addresses'] in session['success_db_email_addresses']:
            session['success_email_addresses'] = session['success_email_addresses']
    elif 'success_db_email_addresses' in session and session['success_db_email_addresses'] != db_email_address:
        session['success_email_addresses'] = db_email_address
    else:
        session['success_db_email_addresses'] = session['success_db_email_addresses']

    if 'winner_message' not in session:
        session['class'] = "alert alert-danger"
    else:
        session.pop('class')
        session['class'] = "alert alert-success"
        session.pop('_flashes', None)
        flash(u'{}'.format(session['winner_message']), 'success')
        session.pop('winner_message')


    if 'success_count' not in session:
        session['success_count'] = 0
        print session['success_count']
    elif session['success_count'] >= 1:
        session.pop('success_count')
        session['success_count'] = 0
        session['class'] = "alert alert-success"
        return redirect('/')
    else:
        session['success_count'] = session['success_count']
        
    return render_template('success.html', all_email_address=db_email_address)

@app.route('/success_form', methods=['GET', 'POST'])
def validate_delete_email():
    
    query = "DELETE FROM email_address_book_db.email_addresses WHERE email_addresses.email_address = :email"
    data = {
        'email': request.form['success_email_address']
    }
    mysql.query_db(query, data)
    if 'success_email_count' not in session:
        session['success_email_count'] = 0
    else:
        session['success_email_count'] = session['success_email_count']

    if len(request.form['success_email_address']) < 1:
        flash(u'Email Address field can not be blank.', 'error')
    elif not EMAIL_REGEX.match(request.form['success_email_address']):
        flash(u'The Email Address is Invalid.', 'error')
    else:
        for success_email_addresses in session['db_email_addresses']:    
            if success_email_addresses['email_address'] == request.form['success_email_address']:
                session['success_count'] += 1
                session['success_winner_message'] = "The email address you entered {} has been deleted from the database!  Thank you!".format(request.form['success_email_address'])
                session.pop('success_email_count')
                session['success_email_count'] = 0
            else:
                session['success_email_count'] += 1
        if session['success_email_count'] > 0:
            flash(u'The Email Address does not exsist within the database', 'error')
            session.pop('success_email_count')
            session['success_email_count'] = 0
    return redirect('/success')
app.run(debug=True)

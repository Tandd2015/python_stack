from flask import Flask, render_template, redirect, session, request, flash
import datetime
import re

EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

app = Flask(__name__)
app.secret_key = "AllKindsOfSecrets!"

@app.route('/')
def registerRoute():
    
    return render_template('index.html')

@app.route('/backTo', methods=['POST'])
def processCenter():

    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] = session['count']

    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] = session['counter']

    if 'counters' not in session:
        session['counters'] = 0
    else:
        session['counters'] = session['counters']
    
    if 'counter2' not in session:
        session['counter2'] = 0
    else:
        session['counter2'] = session['counter2']

    if 'counters2' not in session:
        session['counters2'] = 0
    else:
        session['counters2'] = session['counters2']

    if 'd' not in session:
        session['d'] = datetime.datetime.now().strftime("%d")
    elif 'd' in session and request.method == 'POST':
        session.pop('d')
        session['d'] = datetime.datetime.now().strftime("%d")
    else:
        session['d'] = session['d']

    if 'm' not in session:
        session['m'] = datetime.datetime.now().strftime("%m")
    elif 'm' in session and request.method == 'POST':
        session.pop('m')
        session['m'] = datetime.datetime.now().strftime("%m")
    else:
        session['m'] = session['m']

    if 'y' not in session:
        session['y'] = datetime.datetime.now().strftime("%Y")
    elif 'y' in session and request.method == 'POST':
        session.pop('y')
        session['y'] = datetime.datetime.now().strftime("%Y")
    else:
        session['y'] = session['y']
    
    if len(request.form['email_address']) < 1:
        flash(u'Email Address field can not be blank.','error')
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash(u'The Email Address is Invalid.','error')
    else:
        session['count'] += 1
        session['email'] = request.form['email_address']
    
    if len(request.form['first_name']) >= 1:
        session['count'] += 1
    else:
        flash(u'First Name field can not be blank.','error')

    if len(request.form['first_name']) >= 1 and request.form['first_name'].isalpha():
        session['count'] += 1
        session['firsty'] = request.form['first_name']
    else:
        flash(u'First Name field can not contain numbers.','error')

    if len(request.form['last_name']) >= 1:
        session['count'] += 1
    else:
        flash(u'Last Name field can not be blank.','error')

    if len(request.form['last_name']) >= 1 and request.form['last_name'].isalpha():
        session['count'] += 1
        session['lasty'] = request.form['last_name']
    else:
        flash(u'Last Name field can not contain numbers', 'error')
    
    if len(request.form['password_1']) < 1:
        flash(u'Password field can not be blank.', 'error')
    elif len(request.form['password_1']) >= 1 and len(request.form['password_1']) < 8:
        flash(u'Password field must be 8 characters minimum long.', 'error')
    else:
        session['count'] += 1

    for index in request.form['password_1']:
        
        if index.isupper():
            session['counter'] += 1
        else:
            session['counter'] = session['counter']

        if index.isdigit():
            session['counters'] += 1
        else:
            session['counters'] = session['counters']
    
    if session['counter'] < 1:
        flash(u'Password field must have at least one capital letter.', 'error')
    else:
        session['count'] += 1

    if session['counters'] < 1:
        flash(u'Password field must have at least one number.', 'error')
    else:
        session['count'] += 1

    if len(request.form['password_2']) < 1:
        flash(u'Password Conformation field can not be blank.', 'error')
    elif len(request.form['password_2']) >= 1 and len(request.form['password_2']) < 8:
        flash(u'Password Conformation field must be 8 characters minimum long.', 'error')
    else:
        session['count'] += 1

    for index2 in request.form['password_2']:
        
        if index2.isupper():
            session['counter2'] += 1
        else:
            session['counter2'] = session['counter2']

        if index2.isdigit():
            session['counters2'] += 1
        else:
            session['counters2'] = session['counters2']

    if session['counter2'] < 1:
        flash(u'Password Conformation field must have at least one capital letter.', 'error')
    else:
        session['count'] += 1

    if session['counters2'] < 1:
        flash(u'Password Conformation field must have at least one number.', 'error')
    else:
        session['count'] += 1

    if request.form['password_1'] == request.form['password_2']:
        if session['counter'] >= 1 and session['counters'] >= 1:
            session['password'] = request.form['password_1']
            session.pop('counter', None)
            session['counter'] = 0
            session.pop('counters', None)
            session['counters'] = 0
            session['count'] += 1
        else:
            session.pop('counter', None)
            session['counter'] = 0
            session.pop('counters', None)
            session['counters'] = 0

        if session['counter2'] >= 1 and session['counters2'] >= 1:
            session['password2'] = request.form['password_2']
            session.pop('counter2', None)
            session['counter2'] = 0
            session.pop('counters2', None)
            session['counters2'] = 0
            session['count'] += 1
        else:
            session.pop('counter2', None)
            session['counter2'] = 0
            session.pop('counters2', None)
            session['counters2'] = 0
    else:
        flash(u'Password field and Password Conformation field Must Match.', 'error')
        session.pop('counter', None)
        session['counter'] = 0
        session.pop('counters', None)
        session['counters'] = 0
        session.pop('counter2', None)
        session['counter2'] = 0
        session.pop('counters2', None)
        session['counters2'] = 0

    if len(request.form['day']) < 1:
        flash(u'Day can not be blank', 'error')
    elif len(request.form['day']) >= 1 and int(request.form['day']) > 31:
        flash(u'Invalid Day must be 1 through 31.', 'error')
    else:
        session['count'] += 1
    
    if len(request.form['month']) < 1:
        flash(u'Month can not be blank', 'error')
    elif len(request.form['month']) >= 1 and int(request.form['month']) > 12:
        flash(u'Invalid Month must be 1 through 12.', 'error')
    elif len(request.form['month']) >= 1 and int(request.form['month']) < 13:
        if int(request.form['month']) == int(session['m']) and int(request.form['year']) == int(session['y']):
            if int(request.form['day']) >= int(session['d']):
                flash(u'This Day is a future date. Date must be before todays date.', 'error')
    else:
        session['count'] += 1

    if len(request.form['year']) < 1:
        flash(u'Year can not be blank', 'error')
    elif len(request.form['year']) >= 1 and int(request.form['year']) > int(session['y']):
        flash(u'This Year, Month, and Day is a future date. Date must be before todays date.', 'error')
    elif len(request.form['year']) >= 1 and int(request.form['year']) == int(session['y']):
        if int(request.form['month']) > int(session['m']):
            flash(u'This Month and Day is a future date. Date must be before todays date.', 'error')
    elif len(request.form['year']) >= 1 and int(request.form['year']) <= 1900:
        flash(u'Invalid Year must after 1900.', 'error')
    else:
        session['count'] += 1

    if session['count'] == 16:
        flash(u'Thanks for submitting your information.', 'info')
        session.pop('count')
    else:
        session.pop('count')
    return redirect('/')

app.run(debug=True)

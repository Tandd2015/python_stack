from flask import Flask, render_template, request, session, redirect, flash, url_for
import random, re
app = Flask(__name__)
app.secret_key = 'KeepingSecrets'

@app.route('/')
def load_page():
    if "num" not in session:
        session['num'] = random.randrange(1, 101)
    else: 
        session['num'] = session['num']
    # print (session['num'])
    if "count" not in session:
        session['count'] = 0
    else: 
        session['count'] = session['count']
    # print (session['count'])
    if "v_count" not in session:
        session['v_count'] = 0
    else: 
        session['v_count'] = session['v_count']
    # print (session['v_count'])
    if "winner_count" not in session:
        session['winner_count'] = 0
    else: 
        session['winner_count'] = session['winner_count']
    # print (session['winner_count'])
    return render_template('index.html')

# #---------------NINJA BONUS
# @app.route('/form', methods=['POST'])
# def load_page_form():
#     session['ans'] = request.form.get('user_in', type=int)    
#     if len(request.form['user_in'])<=0:
#         session['v_count']+=1
#         flash('Must have an entry to submit')
#     elif not re.match(r'\d', request.form['user_in']):
#         session['v_count']+=1
#         flash("entry must be a interger")
#     else:
#         session.pop('v_count')
#         session['v_count']= 0
#         if session['ans'] > session['num']:
#             session['winner_count']+=1
#             session['count']+=1
#             flash("too high")
#         elif session['ans'] < session['num']:
#             session['winner_count']+=1
#             session['count']+=1
#             flash("too low")
#         else:
#             session.pop('count')
#             session['count']= 0
#             flash("was the number! Good Job")
#     return redirect('/')

#---------------SENSEI BONUS
@app.route('/form', methods=['POST'])
def load_page_form():
    session['ans'] = request.form.get('user_in', type=int)    
    if len(request.form['user_in'])<=0:
        session['v_count']+=1
        flash('Must have an entry to submit')
    elif not re.match(r'\d', request.form['user_in']):
        session['v_count']+=1
        flash("entry must be a interger")
    else:
        if session['count'] < 5:
            session.pop('v_count')
            session['v_count']= 0
            if session['ans'] > session['num']:
                session['winner_count']+=1
                session['count']+=1
                flash("is too high")
            elif session['ans'] < session['num']:
                session['winner_count']+=1
                session['count']+=1
                flash("is too low")
            else:
                session.pop('count')
                session['count']= 0
                flash("was the number! Good Job")
        else:
            session.pop('v_count')
            session['v_count']= 0
            if session['ans'] > session['num']:
                session['winner_count']+=1
                session['count']+=1
                flash("You Lost. This Geuss %d was too High %d consecutive wrong answers "%(session['ans'], session['winner_count']))
            elif session['ans'] < session['num']:
                session['winner_count']+=1
                session['count']+=1
                flash("You Lost. This Geuss %d was too Low %d consecutive wrong answers "%(session['ans'], session['winner_count']))
            else:
                session.pop('count')
                session['count']= 0
                flash("was the number! Good Job")
    # print(session['v_count'],"session['v_count']")
    # print (session['count'],"session['count']")
    # print (session['ans'],"session['ans']")
    print (session['winner_count'],"session['winner_count']")
    print (session['num'],"session['num']")
    # print(session['v_count'],"session['v_count']")
    # print (session['count'],"session['count']")
    return redirect('/')

@app.route('/clear')
def clear_s():
    session.clear()
    return redirect('/')

@app.route('/cr')
def cr_s():
    session['winner_count'] = 0
    session['num'] = random.randrange(1, 101)
    return redirect('/')

@app.route("/winner_board_form")
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

@app.route('/win')
def winner_board_load_page_1():
        return render_template('win.html')    

@app.route('/winner_board')
def winner_board_load_page_2():
    if 'winners' not in session:
        session['winners'] = []
    else:
        session['winners']= session['winners']
    return render_template('winner.html')

@app.route("/winner_board_form", methods=['POST'])
def winner_board_registeration_validation():
    winner_board_registeration_counter = 0
    session['winner_count']= 1
    if len(request.form['registeration_f_name']) <= 1:
        flash(u'First name field must contain at least one letters', 'error')
    elif charFinder(request.form['registeration_f_name']) == True and len(request.form['registeration_f_name']) >= 1:
        flash(u'First name field can only contain letters', 'error')
    else:
        winner_board_registeration_counter += 1

    if len(request.form['registeration_l_name']) <= 1:
        flash(u'Last name field must contain at least one letters', 'error')
    elif charFinder(request.form['registeration_l_name']) == True and len(request.form['registeration_l_name']) >= 1:
        flash(u'Last name field can only contain letters', 'error')
    else:
        winner_board_registeration_counter += 1
    
    if winner_board_registeration_counter == 2:
        winner= {
            'first_name': request.form['registeration_f_name'],
            'last_name': request.form['registeration_l_name'],
            'attempts': session['winner_count']
        }
        session['winners'].append(winner)
        stopper = True
        while stopper:
            stopper= False
            for i in range(len(session['winners'])-1):
                if int(session['winners'][i]['attempts'])>int(session['winners'][i+1]['attempts']):
                    session['winners'][i], session['winners'][i+1] = session['winners'][i+1] , session['winners'][i]
                    stopper = True
        return redirect('/win')
    # session.clear()
    return redirect('/winner_board')
if __name__ == '__main__':
    app.run(debug=True)
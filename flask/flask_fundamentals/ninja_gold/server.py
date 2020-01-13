from flask import Flask, render_template, redirect, request, session, url_for, flash
import random
import datetime
app = Flask(__name__)
app.secret_key = 'SecretKeyThree'

@app.route('/')
def formGolor():
    if 'log_holder' not in session:
        session['log_holder']=[]
    else:
        session['log_holder']=session['log_holder']

    if 'color_holder' not in session:
        session['color_holder']=[]
    else:
        session['color_holder']=session['color_holder']

    if 'win_lose' not in session:
        session['win_lose']= False
    else:
        session['win_lose']= session['win_lose']
    return render_template('index.html')

@app.route('/clear')
def clear_s():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods = ['GET'])
def sess_for_popper(string1, string2):
    session.pop('count')
    for i in range(15,-1,-1):
        new1= '%s%d' % (string1, i)
        new2= '%s%d' % (string2, i)
        session.pop(new1, None)
        session.pop(new2, None)
    session['count'] = 0
    session['log%s'%session['count']] = session['log']
    session.pop('log_holder')
    session.pop('color_holder')
    session['log_holder'] = []
    session['color_holder'] = []
    session.pop('sumGold')
    session['sumGold']= 0
    if session['count'] == 0 and 'moreGold' not in session:
        if session['sumGold'] >= 0:
            session['color%s' % session['count']] = "text-success"
        else:
            session['color%s' % session['count']] = "text-danger"
    else:
        if session['moreGold'] >= 0:
            session['color%s' % session['count']] = "text-success"
        else:
            session['color%s' % session['count']] = "text-danger"
    session.update()
    return print('Session items updated with current strings %s %s' % (string1, string2))

@app.route('/process_money', methods=['GET', 'POST'])
def goldGolor():
    session['win_lose'] = False
    if request.form['action'] == 'farm':
        session['value'] = "farm"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")

        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(10, 21)
            session['log'] = f"Earned {session['sumGold']} golds from the {session['value']}! ({session['daTime']})"
        else:
            session['moreGold'] = random.randrange(10, 21)
            session['sumGold'] += session['moreGold']
            session['log'] = f"Earned {session['moreGold']} golds from the {session['value']}! ({session['daTime']})"

        if 'count' not in session:
            session['count'] = 0
            session['log%s' % session['count']] = session['log']
            session['color%s' % session['count']]= "text-success"
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])
        elif session['count'] > 14 and session['sumGold'] < 499:
            session['end_color']= "text-danger"
            session['win_lose'] = True
            flash("You Lost. Try Again")
            sess_for_popper("log", "color")
        elif session['count'] <= 15 and session['sumGold'] > 499:
            session['end_color']= "text-success"
            session['win_lose'] = True
            sess_for_popper("log", "color") 
            flash("You Win. Try Again")    
        else:
            session['count'] += 1
            session['color%s' % session['count']]= "text-success"
            session['log%s' % session['count']] = session['log']
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])           
        print(session['log_holder'])
        print(session['color_holder'])
        print(session['count'])
        print(session['win_lose'])
    
    elif request.form['action'] == 'cave':
        session['value'] = "cave"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        
        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(5, 11)
            session['log'] = f"Earned {session['sumGold']} golds from the {session['value']}! ({session['daTime']})"
        else:
            session['moreGold'] = random.randrange(5, 11)
            session['sumGold'] += session['moreGold']
            session['log'] = f"Earned {session['moreGold']} golds from the {session['value']}! ({session['daTime']})"

        if 'count' not in session:
            session['count'] = 0
            session['log%s' % session['count']] = session['log']
            session['color%s' % session['count']]= "text-success"
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])
        elif session['count'] > 14 and session['sumGold'] < 499:
            session['end_color']= "text-danger"
            session['win_lose'] = True
            flash("You Lost. Try Again")
            sess_for_popper("log", "color")
        elif session['count'] <= 15 and session['sumGold'] > 499:
            session['end_color']= "text-success"
            session['win_lose'] = True
            sess_for_popper("log", "color") 
            flash("You Win. Try Again")    
        else:
            session['count'] += 1
            session['color%s' % session['count']]= "text-success"
            session['log%s' % session['count']] = session['log']
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])     
        print(session['log_holder'])
        print(session['color_holder'])
        print(session['count'])
        print(session['win_lose'])
    
    elif request.form['action'] == 'house':
        
        session['value'] = "house"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        
        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(2, 6)
            session['log'] = f"Earned {session['sumGold']} golds from the {session['value']}! ({session['daTime']})"
        else:
            session['moreGold'] = random.randrange(2, 6)
            session['sumGold'] += session['moreGold']
            session['log'] = f"Earned {session['moreGold']} golds from the {session['value']}! ({session['daTime']})"
        
        if 'count' not in session:
            session['count'] = 0
            session['log%s' % session['count']] = session['log']
            session['color%s' % session['count']]= "text-success"
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])
        elif session['count'] > 14 and session['sumGold'] < 499:
            session['end_color']= "text-danger"
            session['win_lose'] = True
            flash("You Lost. Try Again")
            sess_for_popper("log", "color")
        elif session['count'] <= 15 and session['sumGold'] > 499:
            session['end_color']= "text-success"
            session['win_lose'] = True
            sess_for_popper("log", "color") 
            flash("You Win. Try Again")    
        else:
            session['count'] += 1
            session['color%s' % session['count']]= "text-success"
            session['log%s' % session['count']] = session['log']
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])           
        print(session['log_holder'])
        print(session['color_holder'])
        print(session['count'])
        print(session['win_lose'])
    
    else:

        session['value'] = "casino"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        
        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(-50, 51)
        
            if session['sumGold'] >= 0:
                session['log'] = f"Earned {session['sumGold']} golds from the {session['value']}! ({session['daTime']})"
            else: 
                session['log'] = f"Entered a {session['value']} and lost {session['sumGold']} golds... Ouch.. ({session['daTime']})"
        else:
            session['moreGold'] = random.randrange(-50, 51)
            session['sumGold'] += session['moreGold']
            if session['moreGold'] >= 0:
                session['log'] = f"Earned {session['moreGold']} golds from the {session['value']}! ({session['daTime']})"
            else: 
                session['log'] = f"Entered a {session['value']} and lost {session['moreGold']} golds... Ouch.. ({session['daTime']})"

        if 'count' not in session:
            session['count'] = 0
            session['log%s' % session['count']] = session['log']
            session['color%s' % session['count']]= "text-success"
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])
        elif session['count'] > 14 and session['sumGold'] < 499:
            session['end_color']= "text-danger"
            session['win_lose'] = True
            flash("You Lost. Try Again")
            sess_for_popper("log", "color")
        elif session['count'] <= 15 and session['sumGold'] > 499:
            session['end_color']= "text-success"
            session['win_lose'] = True
            sess_for_popper("log", "color") 
            flash("You Win. Try Again")    
        else:
            session['count'] += 1
            if session['count'] == 0 and 'moreGold' not in session:
                if session['sumGold'] >= 0:
                    session['color%s' % session['count']] = "text-success"
                else:
                    session['color%s' % session['count']] = "text-danger"
            else:
                if session['moreGold'] >= 0:
                    session['color%s' % session['count']] = "text-success"
                else:
                    session['color%s' % session['count']] = "text-danger"
            session['log%s' % session['count']] = session['log']
            session['color_holder'].append(session['color%s' % session['count']])
            session['log_holder'].append(session['log%s' % session['count']])
            # elif session['count'] <= 15 and session['sumGold'] > 499:
            #     sess_for_popper("log", "color") 
            #     flash("You Win. Try Again")               
        print(session['log_holder'])
        print(session['color_holder'])
        print(session['count'])
        print(session['win_lose'])
    return redirect(url_for('formGolor'))
if __name__ == '__main__':
    app.run(debug=True)
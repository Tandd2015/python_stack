from flask import Flask, render_template, redirect, request, session, url_for, flash
import random
import datetime
import logging
from logging.handlers import logging
app = Flask(__name__)
app.secret_key = 'SecretKeyThree'

@app.route('/')
def formGolor():
    return render_template('index.html')

@app.route('/process_money', methods=['GET', 'POST'])
def goldGolor():
    
    if request.form['action'] == 'farm':
        
        session['value'] = "farm"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")

        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(10, 21)
            session['log'] = "Earned {} golds from the {}! ({})".format(session['sumGold'], session['value'], session['daTime'])
        else:
            session['moreGold'] = random.randrange(10, 21)
            session['sumGold'] += session['moreGold']
            session['log'] = "Earned {} golds from the {}! ({})".format(session['moreGold'], session['value'], session['daTime'])

        if 'count' not in session:
            session['count'] = 0
            session['log{}'.format(session['count'])] = session['log']
        else:
            session['count'] += 1
            session['log{}'.format(session['count'])] = session['log']
            if session['count'] > 6:
                session.pop('count')
                session.pop('log0', None)
                session.pop('log1', None)
                session.pop('log2', None)
                session.pop('log3', None)
                session.pop('log4', None)
                session.pop('log5', None)
                session.pop('log6', None)
                session.pop('color0', None)
                session.pop('color1', None)
                session.pop('color2', None)
                session.pop('color3', None)
                session.pop('color4', None)
                session.pop('color5', None)
                session.pop('color6', None)
                session['count'] = 0
                session['log{}'.format(session['count'])] = session['log']      
                session.update()
        session['color{}'.format(session['count'])] = "text-success"
    
    elif request.form['action'] == 'cave':
        
        session['value'] = "cave"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        
        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(5, 11)
            session['log'] = "Earned {} golds from the {}! ({})".format(session['sumGold'], session['value'], session['daTime'])
        else:
            session['moreGold'] = random.randrange(5, 11)
            session['sumGold'] += session['moreGold']
            session['log'] = "Earned {} golds from the {}! ({})".format(session['moreGold'], session['value'], session['daTime'])

        if 'count' not in session:
            session['count'] = 0
            session['log{}'.format(session['count'])] = session['log']
        else:
            session['count'] += 1
            session['log{}'.format(session['count'])] = session['log']
            if session['count'] > 6:
                session.pop('count')
                session.pop('log0', None)
                session.pop('log1', None)
                session.pop('log2', None)
                session.pop('log3', None)
                session.pop('log4', None)
                session.pop('log5', None)
                session.pop('log6', None)
                session.pop('color0', None)
                session.pop('color1', None)
                session.pop('color2', None)
                session.pop('color3', None)
                session.pop('color4', None)
                session.pop('color5', None)
                session.pop('color6', None)
                session['count'] = 0
                session['log{}'.format(session['count'])] = session['log']      
                session.update()
        session['color{}'.format(session['count'])] = "text-success"    
    
    elif request.form['action'] == 'house':
        
        session['value'] = "house"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        
        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(2, 6)
            session['log'] = "Earned {} golds from the {}! ({})".format(session['sumGold'], session['value'], session['daTime'])
        else:
            session['moreGold'] = random.randrange(2, 6)
            session['sumGold'] += session['moreGold']
            session['log'] = "Earned {} golds from the {}! ({})".format(session['moreGold'], session['value'], session['daTime'])
        
        if 'count' not in session:
            session['count'] = 0
            session['log{}'.format(session['count'])] = session['log']
        else:
            session['count'] += 1
            session['log{}'.format(session['count'])] = session['log']
            if session['count'] > 6:
                session.pop('count')
                session.pop('log0', None)
                session.pop('log1', None)
                session.pop('log2', None)
                session.pop('log3', None)
                session.pop('log4', None)
                session.pop('log5', None)
                session.pop('log6', None)
                session.pop('color0', None)
                session.pop('color1', None)
                session.pop('color2', None)
                session.pop('color3', None)
                session.pop('color4', None)
                session.pop('color5', None)
                session.pop('color6', None)
                session['count'] = 0
                session['log{}'.format(session['count'])] = session['log']      
                session.update()
        session['color{}'.format(session['count'])] = "text-success"
    
    else:
        
        session['value'] = "casino"
        session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
        
        if 'sumGold' not in session:
            session['sumGold'] = random.randrange(-50, 51)
        
            if session['sumGold'] >= 0:
                session['log'] = "Earned {} golds from the {}! ({})".format(session['sumGold'], session['value'], session['daTime'])

            else: 
                session['log'] = "Entered a {} and lost {} golds... Ouch.. ({})".format(session['value'], session['sumGold'], session['daTime'])
        
        else:
        
            session['moreGold'] = random.randrange(-50, 51)
            session['sumGold'] += session['moreGold']
        
            if session['moreGold'] >= 0:
                session['log'] = "Earned {} golds from the {}! ({})".format(session['moreGold'], session['value'], session['daTime'])

            else: 
                session['log'] = "Entered a {} and lost {} golds... Ouch.. ({})".format(session['value'], session['moreGold'], session['daTime'])
    
        if 'count' not in session:
            session['count'] = 0
            session['log{}'.format(session['count'])] = session['log']
            if session['count'] == 0 and 'moreGold' not in session:
                if session['sumGold'] >= 0:
                    session['color{}'.format(session['count'])] = "text-success"
                else:
                    session['color{}'.format(session['count'])] = "text-danger"
            else:
                if session['moreGold'] >= 0:
                    session['color{}'.format(session['count'])] = "text-success"
                else:
                    session['color{}'.format(session['count'])] = "text-danger"

        else:
            session['count'] += 1
            session['log{}'.format(session['count'])] = session['log']
            if session['count'] == 0 and 'moreGold' not in session:
                if session['sumGold'] >= 0:
                    session['color{}'.format(session['count'])] = "text-success"
                else:
                    session['color{}'.format(session['count'])] = "text-danger"
            else:
                if session['moreGold'] >= 0:
                    session['color{}'.format(session['count'])] = "text-success"
                else:
                    session['color{}'.format(session['count'])] = "text-danger"
            if session['count'] > 6:
                session.pop('count')
                session.pop('log0', None)
                session.pop('log1', None)
                session.pop('log2', None)
                session.pop('log3', None)
                session.pop('log4', None)
                session.pop('log5', None)
                session.pop('log6', None)
                session.pop('color0', None)
                session.pop('color1', None)
                session.pop('color2', None)
                session.pop('color3', None)
                session.pop('color4', None)
                session.pop('color5', None)
                session.pop('color6', None)
                session['count'] = 0
                session['log{}'.format(session['count'])] = session['log']      
                if session['count'] == 0 and 'moreGold' not in session:
                    if session['sumGold'] >= 0:
                        session['color{}'.format(session['count'])] = "text-success"
                    else:
                        session['color{}'.format(session['count'])] = "text-danger"
                else:
                    if session['moreGold'] >= 0:
                        session['color{}'.format(session['count'])] = "text-success"
                    else:
                        session['color{}'.format(session['count'])] = "text-danger"
                session.update()


    # LOGGER Example not using this on this project
    # log = logging.getLogger()
    # log.setLevel(logging.WARNING)
    # formatter = logging.Formatter(session['log'])
    # stream = logging.StreamHandler()
    # stream.setFormatter(formatter)
    # log.addHandler(stream)
    # app.logger.warning(log.addHandler(stream))

    return redirect(url_for('formGolor'))

if __name__ == '__main__':
    app.run(debug=True)

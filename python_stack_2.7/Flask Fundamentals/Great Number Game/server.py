from flask import Flask, render_template, request, session, redirect, flash, url_for
import random
app = Flask(__name__)
app.secret_key = 'SecondSecret'

@app.route('/', methods=['GET', 'POST'])
def loadPage():

    if "geuss" not in session:
        session['geuss'] = random.randrange(1, 101)
    else: 
        session['geuss'] = session['geuss']
    print session['geuss']
    
    if request.method == 'POST':
        session['anwser'] = request.form.get('geussed', type=int)
        print session['anwser']
        if session['anwser'] > session['geuss']:
            flash("too high")
        elif session['anwser'] < session['geuss']:
            flash("too low")
        else:
            flash("was the number! Good Job")
    return render_template('index.html', anwser=request.form.get('geussed', type=int), geuss=session['geuss'])

@app.route('/clear')
def clearS():
    session.pop('geuss', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
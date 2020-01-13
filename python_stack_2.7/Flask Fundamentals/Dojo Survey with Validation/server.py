from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "WhatIsTheSecret!"

@app.route('/')
def startRoute():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def postedInfo():
    
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] = session['count']

    if len(request.form['First_Name']) < 1:
        flash("First Name cannot be empty!")
    else:
        session['fName'] = request.form['First_Name']
        session['count'] += 1    
        
    if len(request.form['Last_Name']) < 1:
        flash("Last Name cannot be empty!")
    else:
        session['lName'] = request.form['Last_Name']
        session['count'] += 1
        
    if request.form['Dojo_Location'] == "Dojo Location":
        flash("Make a Selection. Dojo Location answer was Blank")
    else:
        session['dojoL'] = request.form['Dojo_Location']
        session['count'] += 1
        
    if request.form['Favorite_Language'] == "Favorite Language":
        flash("Make a Selection. Favorite Language answer was Blank")
    else:
        session['favL'] = request.form['Favorite_Language']
        session['count'] += 1
        
    if len(request.form['Text_Area']) > 120:
        flash("Comment Area cannot be over 120 characters")
    else:
        session['textA'] = request.form['Text_Area']
    
    if session['count'] > 3:
        session.pop('count')
        return render_template("results.html")
    else:
        session.pop('count')

    return redirect('/')
app.run(debug=True)
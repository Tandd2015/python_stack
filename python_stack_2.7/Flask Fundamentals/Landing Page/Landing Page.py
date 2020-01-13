from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def routeStart():
    return render_template("index.html", new_phrase="This is the third way I will Greet you on my page", times=3, phrase="HELLO again!!! for the Second time")

@app.route('/ninjas')
def showNinjas():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def AformU():
    return render_template("dojos.html")

@app.route('/dojos/new', methods=['Get', 'POST'])
def AformUpost():
    print "Hello"
    question = request.form['option']
    email = request.form['Email']
    first = request.form['First']
    last = request.form['Last']
    return redirect('/dojos/new')
app.run(debug=True)


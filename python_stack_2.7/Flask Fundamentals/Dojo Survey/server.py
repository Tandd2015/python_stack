from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def startRoute():
    return render_template("index.html")

@app.route('/results', methods=['POST', 'GET'])
def postedInfo():
    Results = request.form
    print Results
    return render_template("results.html", Results = request.form)
app.run(debug=True)
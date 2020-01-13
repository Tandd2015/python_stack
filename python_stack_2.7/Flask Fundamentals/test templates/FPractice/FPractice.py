from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    students = ["verionka", "ninos", "edward", "fariha"]
    return render_template("index.html", name="daniel", students=students)

@app.route("/hello")
def index1():
    print "hello world! Again!"
    return redirect("/")

@app.route("/process", methods=["POST"])
def process():
    print request.form
    print request.form["first_name"]
    print request.form["last_name"]
    return render_template("index.html", name=request.form["first_name"])
   #return "got data"

@app.route("/hello/<name>")
def hello_name(name):
    return name

app.run(debug=True)

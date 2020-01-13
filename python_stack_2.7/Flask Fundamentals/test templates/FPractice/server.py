from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "my super secret key"

@app.route("/")
def index():
    if "users" not in session:
        session["users"] = []
    if "logged_user_id" in session:
        return redirect("/dashboard")
    # session["name"] = "Daniel"
    # return redirect("/display_name")
    return render_template("index1.html", all_users=session["users"])
    
@app.route("/register", methods=["POST"])
def register():
# @app.route("/display_name")
# def display_name():
    print "got to register"
    if "users" not in session:
        session["users"] = []
    if "count" not in session:
        session["count"] =  1
    newUser = {
        "id":session["count"],
        "email":request.form["email"],
        "password":request.form["password"]
    }
    # users = []
    # users.append(newUser)
    session["count"] = session["count"] + 1
    print "about to append"
    session["users"].append(newUser)
    # return session["name"]
    session.modified = True
    print "redirecting"
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    for user in session["users"]:
        if user["email"] == email and user["password"] == password:
            session["logged_user_id"] = user["id"]
            return redirect('/dashboard')
            # return "success"
    flash("Password and email wrong")
    return redirect("/")
    # return "failed"
    # return redirect("/")
@app.route("/dashboard")
def dashboard():
    if "logged_user_id" not in session:
        return redirect("/")
    for user in session["users"]:
        if user["id"] == session["logged_user_id"]:
            # return "Welcome to my page, {}".format(user["email"])
            return render_template("success.html", email=user["email"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

app.run(debug=True)
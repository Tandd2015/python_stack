from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('connecting_to_a_database')	# call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends=friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    mysql = connectToMySQL('connecting_to_a_database')
    query = "INSERT INTO connecting_to_a_database (first_name, last_name, occupation, created_at, updated_at) VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());"
    data = {
        "fn": request.form['fname'],
        "ln": request.form['lname'],
        "occup": request.form['occ']
    }
    new_friend_id = mysql.query_db(query,data)
    print(request.form)
    return redirect('/')
                                                        # redirecting. Always redirect after handling POST data to avoid data being handled more than once!
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    return redirect("/show")	                        # changed this line
                                                        # adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")
if __name__ == "__main__":
    app.run(debug=True)
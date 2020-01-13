#------ HELLO.PY------ ITS THE SERVER FILE
from flask import Flask,render_template # Import Flask to allow us to create our app, added render_template!
app = Flask(__name__)                   # Create a new instance of the Flask class called "app"

@app.route('/')                         # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'               # Return the string 'Hello World!' as a response

@app.route('/1')                         # Then in our code, we refer to our HTML files like so: 
def hello_world1():                      # Instead of returning a string, 
    return render_template('index.html')# we'll return the result of the render_template method, passing in the name of our HTML file 
                                        # render_template -- that allows us to return the rendered HTML, we are handling the root route, or '/', route with the hello_world function which renders the index.html
                                        # HTTP verb is "GET".
@app.route('/2')                        #------TEMPLATE ENGINES
def index():                            #- There are 2 special inputs we can use to insert Python-like code into our Flask templates  ({{ some variable }},{% some expression %})
    return render_template("index.html", phrase="hello", times=5)# notice the 2 new named arguments!
                                        #- IMPORTANT:HTML comments (<!-- -->) will NOT comment out Jinja,Jinja commenting syntax instead.

@app.route('/lists')                    #------PASSING LISTS TO JINJA
def render_lists():
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)
@app.route('/success')                  #------ROUTES
def success():                          #-  A route is a variable name we assign to a request. route's communicate to the server what kind of information the client needs.
    return "success"                    #- Every route has two parts: 1.HTTP method (GET, POST, PUT, PATCH, DELETE) 2.URL
                                        #- 2 routes-- 1. localhost:5000/, hello_world function will run -- 2. localhost:5000/success, success function will run.

                                        #- variable rules
@app.route('/hello/<name>')             # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
                                        #- We can add as many of these as we need <____> , giving each variable a different name
@app.route('/users/<username>/<id>')    # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
                                        #-localhost:5000 part of the route determines which server to call upon. The rest of the route, including the "/", tells the server which function should be invoked.
# if request.form['which_form'] == 'register':
#     #do registration process
# elif request.form['which_form'] == 'login':
#     #do login process

# def index():
#     message = "<ul><li>Hello</li></ul>"
#     return render_template("index.html", message=message)


if __name__=="__main__":    # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)     # Run the app in debug mode.


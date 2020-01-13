from flask import Flask , render_template # Import flask to allow us to create our app.
app = Flask(__name__) # Global variable __name__ tells Flask whether or not we are running the file
                      # directly, or importing it as a module.
@app.route('/') # the "@" symbol desinates a "decorator" which attaches the following
                #function to the '/' route. This means that whenever we send a request to
                #localhost:5000/ we will run the following "hello_world" function.
def hello_world(): 
    return render_template("index2.html", firstN="daniel", lastN="beatty", memo="Remeber the name!!!")
app.run(debug=True) # Run the app in debug mode
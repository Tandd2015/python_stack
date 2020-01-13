from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')                             # our index route will handle rendering our form
def index():                                #- write a function that will show a page with a form on it.
    return render_template("index.html")

@app.route('/users', methods=['POST'])      #-Specifying Allowed Methods: methods=['POST'],If we don't provide a value for methods, only GET requests are allowed.
def create_user():
    print("Got Post Info")
    print(request.form)                     #-see what's in your request object, try printing request.form.
    name_from_form = request.form['name']   #-Accessing Data: request.form['name_of_input'],The name we gave to each HTML input was significant.
    email_from_form = request.form['email'] #-server side access data that was input into a field from a user through the request.form dictionary by providing the name of the input as the key.
    return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)
if __name__ == "__main__":                  #-note that the type of anything that comes in through request.form will be a "string" no matter what.
    app.run(debug=True)                     #-value to be identified as an actual number you'll have to type cast it.
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>/<id>')
def show_user_profile(username):
    print username
    print id
    return render_template('user.html')

@app.route('/route/with/<vararg>')
def handler_function(vararg):
    print "hello world"
    # here you can use the variable "vararg" if you want to see what 
    # our arugment looks like 
    print vararg
app.run(debug=True)


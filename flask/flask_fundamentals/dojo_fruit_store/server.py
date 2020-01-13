from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    count=int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    message="Charging %s %s for %d fruits on %s"%(request.form['first_name'], request.form['last_name'], count, datetime.now())
    print(message)
    return render_template("checkout.html", dic=request.form, messages=message)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


#--------------ANSWER------ I notcied that all of the form submission data remains the same but my datetime.now() parameter of my message string variable 
                        #   i beleives it would take another request and response cycle from the root route to update the request form object since it was
                        #   cached to memory
if __name__=="__main__":   
    app.run(debug=True)    
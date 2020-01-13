from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def hello_world():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':    
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index4.html", phrase="The World is Mine", times=6)
app.run(debug=True)
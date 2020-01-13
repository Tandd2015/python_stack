from flask import Flask, render_template, url_for
app= Flask(__name__)

@app.route('/play')
def play1():
    return render_template('index.html', x=3, color='blue')

@app.route('/play/<x>')
def play2(x):
    return render_template('index.html', x=int(x), color='blue')

@app.route('/play/<x>/<color>')
def play3(x, color):
    return render_template('index.html', x=int(x), color=color)

if __name__=="__main__":
    app.run(debug=True)
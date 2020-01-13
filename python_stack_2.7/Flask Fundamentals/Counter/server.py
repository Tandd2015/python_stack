from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'FirstSecret'

@app.route('/', methods=['GET', 'POST'])
def countStart():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] = session['count'] + 1
    print session['count']
    return render_template("index.html")

@app.route('/twoAdd')
def counterTwo():
    session['count'] += 1
    return redirect('/')

@app.route('/clear')
def clearSession():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
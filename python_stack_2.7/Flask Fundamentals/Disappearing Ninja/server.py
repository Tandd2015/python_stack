from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def routeStarter():
    return render_template('noNinja.html')

@app.route('/ninja')
def ninjaGo():
    return render_template('allNinjas.html')

@app.route('/ninja/', defaults={'color' : 'img/notapril.jpg'})
@app.route('/ninja/<color>')
def ninjaHandler(color):
    if color == "blue":
        color = "img/leonardo.jpg"
        print color
        return render_template('Ninja.html', color=color)
    elif color == "red":
        color = "img/raphael.jpg"
        print color
        return render_template('Ninja.html', color=color)
    elif color == "orange":
        color = "img/michelangelo.jpg"
        print color
        return render_template('Ninja.html', color=color)
    elif color == "purple":
        color = "img/donatello.jpg"
        print color
        return render_template('Ninja.html', color=color)
    else:
        color = "img/notapril.jpg"
        print color
        return render_template('Ninja.html', color=color)

if __name__ == '__main__':
    app.run(debug=True)
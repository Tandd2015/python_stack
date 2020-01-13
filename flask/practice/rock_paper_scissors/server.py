from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


#route for storing rock
@app.route('/rock')
def rock():
    session['hand'] = 'rock'
    print("User chose Rock!")
    return redirect('/')

#route for storing paper
@app.route('/paper')
def paper():
    session['hand'] = 'paper'
    print("User chose Paper!")
    return redirect('/')


#route for storing scissors
@app.route('/scissors')
def scissors():
    session['hand'] = 'scissors'
    print("User chose Scissors!")
    return redirect('/')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    #generate random rock, paper, or scissors
    randInt = int(random.random() * 3)
    print(randInt)
    if randInt == 0:
        comHand = 'rock'
    elif randInt == 1:
        comHand = 'paper'
    else:
        comHand = 'scissors'
    print(comHand)
    #compare and find winner
    if(session['hand'] == 'rock'):
        if(comHand == 'paper'):
            result = "YOU LOSE! LOSER!"
        if(comHand == 'scissors'):
            result = "WINNER WINNER CHICKEN DINNER!"
        else:
            result = "TIE, PLAY AGAIN"
    if(session['hand'] == 'paper'):
        if(comHand == 'rock'):
            result = "YOU WIN!!!"
        if(comHand == 'scissors'):
            result = 'YOUR MOM DOESNT LOVE YOU!' 
        else:
            result = "TIE, PLAY AGAIN"
    if(session['hand'] == 'scissors'):
        if(comHand == 'rock'):
            result = "YOU LOSE DUDE! LOST!!!"   
        if(comHand == 'paper'):
            result = "YOU WIN!!!"
        else:
            result = "TIE GAME, PLAY AGAIN!" 
    print(result)
    mylist = [1,2,3,4,5,6,7,8,9]   
    return render_template("result.html", r=result, comHand=comHand)




if __name__=="__main__":
    app.run(debug=True)
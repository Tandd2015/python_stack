from flask import Flask, url_for, render_template
app= Flask(__name__)

@app.route('/')
def checkerboard8_by8():
    return render_template('index.html',y=8,x=8,color_1='red',color_2='black')

@app.route('/<x>')
def checkerboard_var_by8(x):
    return render_template('index.html',x=int(x),y=8,color_1='red',color_2='black')

@app.route('/<x>/<y>')
def checkerboard_var_by_var(x,y):
    return render_template('index.html',x=int(x),y=int(y),color_1='red',color_2='black')

@app.route('/<x>/<y>/<color_1>/<color_2>')
def checkerboard_2var_2color(x,y,color_1,color_2):
    return render_template('index.html',x=int(x),y=int(y),color_1=color_1,color_2=color_2)
if __name__=="__main__":
    app.run(debug=True)
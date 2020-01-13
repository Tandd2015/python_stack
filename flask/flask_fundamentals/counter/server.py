from flask import Flask, render_template, request, session, redirect
import base64
app= Flask(__name__)
app.secret_key= 'gottaSecret1'

@app.route('/')
def root_route_renderer():
    if 'count1' not in session:
        session['count1']= 1
    else:
        session['count1']+= 1

    if 'count' not in session:
        session['count']= 1
    else:
        session['count']+= 1
    return render_template('index.html')

@app.route('/destroy_session')
def session_destroyer():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add_2():
    session['count']+=1
    return redirect('/')

@app.route('/add_var', methods=['POST'])
def adding_var():
    if request.form['count_increaser']=='':
        session['count']+=(-1)
    else:
        session['count']+=(int(request.form['count_increaser'])-1)  
    return redirect('/')

@app.route('/cookie_cutter', methods = ['GET'])
def cookies():
    cookie_var=''
    cookie = request.cookies['session']
    for crumb in cookie:
        if crumb != '.':
            cookie_var+=crumb
        elif crumb == '.':
            session.pop('cookie_holder', None)
            session['cookie_holder']= base64.urlsafe_b64decode('%s==='%cookie_var)
            break
    print (session['cookie_holder'])
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)


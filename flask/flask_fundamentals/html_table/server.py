from flask import Flask, url_for, render_template
app= Flask(__name__)

users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

@app.route('/')
def declare_and_send():
    for user in range(len(users)):
        users[user]['full_name']= users[user]['first_name']+' '+users[user]['last_name']
    return render_template('index.html', users=users)

if __name__=='__main__':
    app.run(debug=True)
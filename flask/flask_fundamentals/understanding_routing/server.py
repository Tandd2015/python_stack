from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def load_root():
    # adapter= app.url_map.bind('')
    # if adapter.match('/'):
    return "<h1>Hello World!</h1>"

@app.route('/dojo')
def load_root_ext():
    return "<h2>Dojo!</h2>"

@app.route('/say/<var>')
def root_ext_2_w_var(var):
    for i in var:
        if i.isalpha()==False:
            return "character not a letter invalid response"
    return "<h3>Hi %s!<h3>"%(var)

@app.route('/repeat/<num>/<var1>')
def root_ext_3_w_2var(num,var1):
    for d in num:
        if d.isdigit()==False:
            return "character not a number invalid response"

    for i in var1:
        if i.isalpha()==False:
            return "character not a letter invalid response"
    return "<p>%s</p>\n"%var1*int(num)

@app.route("/<invalid_urls>")
def url_validator(invalid_urls):
    return "<h1>Sorry No Response Try Again. %s"%invalid_urls

# The other way to do this is to tap into the 404 error handler of Flask @ http://flask.pocoo.org/docs/1.0/patterns/errorpages/
# @app.errorhandler(404)
# def catch_all(err):
#     return "Sorry No Response, Try Again"
if __name__=="__main__":
    app.run(debug=True)
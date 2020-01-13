from flask import Flask, url_for, render_template, request, redirect
app= Flask(__name__)

@app.route('/')
def root_load():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result_load():
    return render_template('results.html', r=request.form)
if __name__ == '__main__':
    app.run(debug=True)
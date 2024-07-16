from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/cat')
def success():
    return 'You selected CAT'

@app.route('/dog')
def failure():
    return 'You selected DOG'

@app.route('/wrong')
def failure():
    return 'Select either CAT or DOG'

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        value = request.form['nm']
        if value == 'cat':
            return redirect(url_for('cat'))
        if value == 'dog':
            return redirect(url_for('dog'))
        else:
            return redirect(url_for('wrong'))
    else:
        return redirect(url_for('wrong'))

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)

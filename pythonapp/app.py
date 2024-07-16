from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/cat')
def cat():
    return "You Chose CAT"

@app.route('/dog')
def dog():
    return "You Chose DOG"

@app.route('/wrong')
def wrong():
    return "Chose CAT or DOG"

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        value = request.form['nm']
        if value == 'cat':
            return redirect(url_for('cat'))
        elif value == 'dog':
            return redirect(url_for('dog'))
        else:
            return redirect(url_for('wrong'))
    else:
        return redirect(url_for('wrong'))

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success')
def success():
    return 'You are correct'

@app.route('/failure')
def failure():
    return 'You are wrong'

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        value = request.form['nm']
        if value == 'no':
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))
    else:
        return redirect(url_for('failure'))

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)

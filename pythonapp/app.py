from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/cat')
def success():
    return render_template('cat.html')

@app.route('/dog')
def failure():
    return render_template('dog.html')

@app.route('/wrong')
def failure():
    return render_template('dog.html')

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

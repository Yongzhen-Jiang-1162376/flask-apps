from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return login_the_user(request.form['username'])
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

def valid_login(username, password):
    pass

def login_the_user(username):
    pass
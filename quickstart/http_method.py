from flask import Flask

app = Flask(__name__)

@app.get('/login')
def login_get():
    return 'login get'

@app.post('/login')
def login_post():
    return 'login post'

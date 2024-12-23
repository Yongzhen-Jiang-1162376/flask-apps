from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(render_template('cookies.html'))
    resp.set_cookie('username', 'Larry Jiang')
    return resp

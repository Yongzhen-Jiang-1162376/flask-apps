from flask import Flask, render_template, make_response, abort

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Somthing'] = 'A value'
    return resp

@app.route('/')
def index():
    abort(404)

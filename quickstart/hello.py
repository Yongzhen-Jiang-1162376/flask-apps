from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# input_name = f'<script>alert("bad")</script>'

# @app.route('/')
# def hello_world():
    # return f'Hello, {escape(input_name)}!'
    # return f'Hello, {input_name}!'

@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/projects')
def project():
    return 'The projects page'

# @app.route('/projects/')
# def projects():
#     return 'The projects/ page'

@app.route('/about')
def about():
    return 'The about page'


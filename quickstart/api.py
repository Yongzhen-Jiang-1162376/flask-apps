from flask import Flask, url_for, jsonify

app = Flask(__name__)


@app.route('/me')
def me_api():
    # return {
    #     'logger': app.logger.name
    # }
    return {
        'usernmae': 'larjia',
        'theme': 'light',
        'image': url_for('static', filename='images/newzealand.png')
    }

@app.route('/users')
def users_api():
    users = [
        {
            'username': 'larjia',
            'email': 'yongzhen.jiang@gmail.com'
        },
        {
            'username': 'johnsmith',
            'email': 'johnsmith@gmail.com'
        }
    ]
    return jsonify(['larjia', 'johnsmith'])
    # return [user for user in users]
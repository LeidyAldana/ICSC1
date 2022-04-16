from flask import Flask
from flask import render_template
from flask import make_response
from flask import request
from flask import redirect
from flask import url_for
from datetime import datetime
import jwt  # PyJWT==0.4.3
import os


app = Flask(__name__)
app.config.update({
    'SECRET_KEY': os.urandom(32)
})


def generate_token(username):
    return jwt.encode({
        'username': username,
        'is_admin': True,
        'flag': os.getenv('FLAG'),
        'iat': datetime.utcnow()
        },
        app.config.get('SECRET_KEY'),
        algorithm='HS256'
    ).decode()


def decode_token(token):
    try:
        return jwt.decode(token, app.config.get('SECRET_KEY'), algorithms=['HS256'])
    except:
        return None


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username') or 'guest'
    token = generate_token(username)
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('token', token)
    return resp


@app.route('/', methods=['GET'])
def index():
    token = request.cookies.get('token')
    if token is None:
        return render_template('index.html')
    
    try:
        data = decode_token(token, app.config.get('SECRET_KEY'))
    except:
        return render_template('index.html', error='Error: invalid token')

    if data.get('is_admin'):
        return render_template('index.html', flag=os.getenv('FLAG'))
    else:
        return render_template('index.html', flag=os.getenv('FLAG'))
    
    username = data.get('username')
    return render_template('index.html', message=f'Welcome {username}!')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

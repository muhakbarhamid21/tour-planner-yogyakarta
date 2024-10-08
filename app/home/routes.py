import os, jwt

from flask import Blueprint, render_template
from flask import request

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    token_valid = False
    token = request.cookies.get('token', None)

    if token:
        try:
            jwt.decode(token, os.environ.get("SECRET_KEY", None), algorithms=['HS256'])
            token_valid = True
        except jwt.ExpiredSignatureError:
            pass
        except jwt.InvalidTokenError:
            pass

    return render_template('home/index.html', token_valid=token_valid)  # Ensure this path matches the actual template location

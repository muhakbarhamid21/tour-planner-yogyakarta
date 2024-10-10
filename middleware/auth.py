from flask import jsonify
from functools import wraps
from flask import request, redirect, url_for
import jwt, os
from dotenv import load_dotenv

load_dotenv()


class AuthMiddleware:
    def __init__(self, app, secret_key):
        self.app = app
        self.secret_key = secret_key
        self.app.before_request(self.check_token)  # Middleware hook sebelum request

    def check_token(self):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403


def is_authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')
        if token:
            try:
                # Decode token dengan secret key dan algoritma yang sesuai
                jwt.decode(token, os.environ.get("SECRET_KEY", "secret-key"), algorithms=['HS256'])
                return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                pass
            except jwt.InvalidTokenError:
                pass
        # Jika token tidak valid atau tidak ada, redirect ke halaman signin
        return redirect(url_for('accounts.signin'))
    return decorated_function

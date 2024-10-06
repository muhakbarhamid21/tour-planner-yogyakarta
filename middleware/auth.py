from flask import request, jsonify
import jwt

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

import jwt, os
from flask import request

SECRET_KEY = os.getenv('SECRET_KEY')


def decode_jwt():
    token = request.cookies.get('token')  # Atau dari request header sesuai kebutuhan Anda
    if not token:
        return None

    try:
        # Decode token menggunakan secret key dan algoritma yang sama dengan yang digunakan untuk encode
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_payload  # Return seluruh payload, yang berisi user detail
    except jwt.ExpiredSignatureError:
        print("Token is expired. Please")
        return None
    except jwt.InvalidTokenError:
        print("Invalid token. Please")
        return None

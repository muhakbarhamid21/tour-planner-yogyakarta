import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from core.database import db
from middleware.auth import is_authenticated

class AuthServices:

    @staticmethod
    def register_user(username, email, password):
        """Registrasi _user baru"""
        # Cek apakah username atau email sudah terdaftar
        user = User.query.filter((User.username == username) | (User.email == email)).first()
        if user:
            return {"message": "Username or Email already exists"}, 400

        # Hash password sebelum disimpan
        hashed_password = generate_password_hash(password, method='sha256')

        # Buat _user baru dan simpan ke database
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

    @staticmethod
    def login_user(username, password):
        """Login _user"""
        # Cari _user berdasarkan username
        user = User.query.filter_by(username=username).first()
        print(user, username, password)
        if not user:
            return False, "User is not registered", {}

        # Verifikasi password
        if not check_password_hash(user.password, password):
            return False, "Invalid Credentials", {}

        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_admin": user.is_admin,
            "fullname": user.fullname
        }
        return True, "Login Successfully", user_data


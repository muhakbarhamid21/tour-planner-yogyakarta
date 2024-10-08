from app.models import User
from core.database import db


class AuthService:

    @staticmethod
    def register_user(username, email, password, is_admin=False):
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return False, "Username or Email Already Exists"

        user = User(username=username, email=email, is_admin=is_admin)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return True, "User Registered"

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return True, "Logged in successfully"
        return False, "Invalid Credentials"
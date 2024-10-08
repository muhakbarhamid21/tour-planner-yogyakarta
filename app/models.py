from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from core.database import db


class User(db.Model):
    __tablename__ = 'account_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    fullname = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        print(self.password, password, end="ini dump check")
        return check_password_hash(self.password, password)


class Attraction(db.Model):
    __tablename__ = 'tourist_attractions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    entry_price = db.Column(db.Float, nullable=False)
    facility = db.Column(db.Float, nullable=False)
    stars = db.Column(db.Float, nullable=False)
    reviews = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('account_users.id'), nullable=False)

    # Relationship
    user = db.relationship('AccountUsers', backref=db.backref('tourist_attractions', lazy=True))


class Weight(db.Model):
    __tablename__ = 'dss_weight'
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    attraction_id = db.Column(db.Integer, db.ForeignKey('attractions.id'), nullable=False)

    # Relationship
    attraction = db.relationship('Attraction', backref=db.backref('bobots', lazy=True))
    sub_parameters = db.relationship('SubParameter', backref='bobot', cascade="all, delete-orphan")


class SubParameter(db.Model):
    __tablename__ = 'sub_parameters'
    id = db.Column(db.Integer, primary_key=True)
    bobot_id = db.Column(db.Integer, db.ForeignKey('bobot.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    # Additional attribute for Rating sub-parameter
    is_rating = db.Column(db.Boolean, nullable=False, default=False)

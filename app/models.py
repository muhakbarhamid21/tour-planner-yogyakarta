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


class AttractionCategory(db.Model):
    __tablename__ = 'tourist_attraction_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('account_users.id'), nullable=False)

    # Relationship
    # user = db.relationship('account_users', backref=db.backref('tourist_attraction_categories', lazy=True))


class Attraction(db.Model):
    __tablename__ = 'tourist_attractions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    entry_price = db.Column(db.Float, nullable=False)
    facility = db.Column(db.Float, nullable=False)
    stars = db.Column(db.Float, nullable=False)
    reviews = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('account_users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('tourist_attraction_categories.id'), nullable=True)

    # Relationship
    # user = db.relationship('account_users', backref=db.backref('tourist_attractions', lazy=True))
    # category = db.relationship('tourist_attraction_categories', backref=db.backref('tourist_attractions', lazy=True))


class Weight(db.Model):
    __tablename__ = 'dss_weights'
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float, nullable=False)
    entry_price = db.Column(db.Float, nullable=False)
    facility = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    stars = db.Column(db.Float, nullable=False)
    reviews = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # attraction_type = db.Column(db.Integer, db.ForeignKey('tourist_attraction_categories.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('account_users.id'), nullable=False)

    # Relationship
    # user = db.relationship('account_users', backref=db.backref('dss_weights', lazy=True))


class Criteria(db.Model):
    __tablename__ = 'dss_criteria'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    key = db.Column(db.String(100), nullable=False)
    criteria = db.Column(db.String(100), nullable=False, default='cost')

    user_id = db.Column(db.Integer, db.ForeignKey('account_users.id'), nullable=False)
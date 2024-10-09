from core.database import db, migrate
from flask import Flask

from app.dash.routes import dash_bp
from app.demo.routes import demo_bp
from app.home.routes import home_bp
from app.tourist.routes import tourist_bp
from app._admin.routes import admin_bp
from app._user.routes import user_bp
from app.authentication.routes import accounts_bp
from app._guest.routes import guest_bp

import os

# Define the path to templates and static folders inside the app directory
template_dir = os.path.join('templates')
static_dir = os.path.join('static')


def create_app():
    # Initialize the Flask app with the specified template and static folder paths
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():

        # Register Blueprints
        app.register_blueprint(dash_bp)
        app.register_blueprint(tourist_bp)
        app.register_blueprint(demo_bp)

        app.register_blueprint(home_bp)
        app.register_blueprint(accounts_bp)
        app.register_blueprint(guest_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(admin_bp)

    return app

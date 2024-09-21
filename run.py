from flask import Flask
from apps.home.routes import home_bp
from apps.admin.routes import admin_bp
from apps.user.routes import user_bp
from apps.authentication.routes import accounts_bp
from apps.guest.routes import guest_bp
import os

# Define the path to templates and static folders inside the apps directory
template_dir = os.path.join(os.path.abspath('apps'), 'templates')
static_dir = os.path.join(os.path.abspath('apps'), 'static')

# Initialize the Flask app with the specified template and static folder paths
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(accounts_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True)

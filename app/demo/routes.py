from flask import Blueprint, render_template
from .services import DemoServices

demo_bp = Blueprint('users', __name__, url_prefix="/demo")


@demo_bp.route('/users', methods=['GET', 'POST'])
def get_users():
    users = DemoServices.get_all_users()
    return render_template("_admin/dashboard-admin.html", users=users)

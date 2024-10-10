# Define routes for Admin pages

from flask import Blueprint, render_template
from .services import AdminService

admin_bp = Blueprint('_admin', __name__)


@admin_bp.route('/admin/dashboard-admin')
def dashboard_admin():
    return render_template('_admin/dashboard-admin.html')


@admin_bp.route('/admin/manage-users')
def manage_users():
    users = AdminService.get_users()
    data = {
        "users": users
    }
    return render_template('_admin/manage-users.html', **data)


@admin_bp.route('/admin/manage-admins')
def manage_admins():
    return render_template('_admin/manage-admins.html')

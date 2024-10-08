# Define routes for Admin pages

from flask import Blueprint, render_template

admin_bp = Blueprint('_admin', __name__)


@admin_bp.route('/admin/dashboard-admin')
def dashboard_admin():
    return render_template('_admin/dashboard-admin.html')


@admin_bp.route('/admin/manage-users')
def manage_users():
    return render_template('_admin/manage-users.html')


@admin_bp.route('/admin/manage-admins')
def manage_admins():
    return render_template('_admin/manage-admins.html')

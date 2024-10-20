# Define routes for Admin pages

import os
from flask import Blueprint, redirect, render_template, url_for, request
import jwt

from middleware.auth import is_authenticated
from .services import AdminService

admin_bp = Blueprint('_admin', __name__)


@admin_bp.route('/admin/dashboard-admin')
def dashboard_admin():
    return render_template('_admin/dashboard-admin.html')


@admin_bp.route('/admin/manage-users')
@is_authenticated
def manage_users():
    
    token = request.cookies.get('token')

    if not token:
        return redirect(url_for('accounts.signin'))
    try:
        decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        username_data = {"username": decoded_token.get('username')}
    except jwt.ExpiredSignatureError:
        return redirect(url_for('accounts.signin'))
    except jwt.InvalidTokenError:
        return redirect(url_for('accounts.signin'))
            
    users = AdminService.get_users()
    
    data = {
        "users": users,
        "username": username_data
    }
    
    return render_template('_admin/manage-users.html', **data)


@admin_bp.route('/admin/manage-admins')
def manage_admins():
    return render_template('_admin/manage-admins.html')

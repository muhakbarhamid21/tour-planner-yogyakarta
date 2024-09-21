from flask import Blueprint, render_template

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts/login')
def login():
    return render_template('accounts/login.html')

@accounts_bp.route('/accounts/register')
def register():
    return render_template('accounts/register.html')
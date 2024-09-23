from flask import Blueprint, render_template

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts/signin')
def signin():
    return render_template('accounts/signin.html')

@accounts_bp.route('/accounts/signup')
def signup():
    return render_template('accounts/signup.html')
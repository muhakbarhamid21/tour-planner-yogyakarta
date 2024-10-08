import os

from .services import AuthServices

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, make_response
import jwt
import datetime


accounts_bp = Blueprint('accounts', __name__)


@accounts_bp.route('/accounts/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        success, message, user_data = AuthServices.login_user(username, password)
        if success:
            # Generate JWT token
            token = jwt.encode({
                "id": user_data.get('id'),
                'username': user_data['username'],
                'email': user_data['email'],
                'is_admin': user_data['is_admin'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, os.getenv('SECRET_KEY'))

            # Create response and set token in cookies
            resp = make_response(redirect(url_for('home.index')))
            resp.set_cookie('token', token)

            return resp
        return render_template('accounts/signin.html', message=message), 401

    return render_template('accounts/signin.html')


@accounts_bp.route('/accounts/signup', methods=["GET", "POST"])
def signup():
    """Route untuk menampilkan form registrasi dan memproses registrasi"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        success, message = AuthServices.register_user(username=username, email=email, password=password)
        if success:
            return redirect(url_for('accounts.signin'))
        return render_template('accounts/signup.html', message=message), 400

    # Jika metode GET, tampilkan form registrasi
    return render_template('accounts/signup.html')
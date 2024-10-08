from flask import Blueprint, render_template, request
import jwt, os
from middleware.auth import is_authenticated
from .services import AuthService

dash_bp = Blueprint('dash', __name__, root_path="/dashboard")

"""
Note of menus

-- _admin
> manage _user
> manage _admin
> dashboard _admin

-- _user
> manage tourism (alternative)

-- guess
> dashboard 
> tourist-attraction
> weight-config
> analysis
> results
"""


@dash_bp.route('/dashboard', methods=['GET'])
@is_authenticated
def dashboard():
    token = request.cookies.get('token')

    data = {}

    cookies_data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
    return render_template("dash/index.html", data=data)
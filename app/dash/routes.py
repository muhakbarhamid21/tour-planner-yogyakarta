from flask import Blueprint, render_template, request
import jwt, os
from .services import AuthService

dash_bp = Blueprint('dash', __name__, root_path="/dashboard")

"""
Note of menus

-- admin
> manage user
> manage admin
> dashboard admin

-- user
> manage tourism (alternative)

-- guess
> dashboard 
> tourist-attraction
> weight-config
> analysis
> results
"""


@dash_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    token = request.cookies.get('token')

    data = {}

    cookies_data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
    print(cookies_data)
    return render_template("dash/index.html", data=data)
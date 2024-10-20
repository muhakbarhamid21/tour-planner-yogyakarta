from flask import Blueprint, redirect, render_template, request, url_for
import jwt, os
from app.dash.services2 import get_attraction_count_for_category
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
> manage tourist (alternative)

-- guess
> dashboard 
> tourist-attraction
> weight-config
> analysis
> results
"""
from flask import g

@dash_bp.route('/dashboard', methods=['GET'])
@is_authenticated
def dashboard():
    token = request.cookies.get('token')
    
    count_category_1 = get_attraction_count_for_category(1)
    count_category_2 = get_attraction_count_for_category(2)
    count_category_3 = get_attraction_count_for_category(3)
    count_category_4 = get_attraction_count_for_category(4)
    
    # GET USERNAME
    if not token:
        return redirect(url_for('accounts.signin'))
    try:
        decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        username = decoded_token.get('username')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('accounts.signin'))
    except jwt.InvalidTokenError:
        return redirect(url_for('accounts.signin'))
    username = {
        "username": username
    }
    
    data = {
        "count_category_1": count_category_1,
        "count_category_2": count_category_2,
        "count_category_3": count_category_3,
        "count_category_4": count_category_4,
    }
    
    cookies_data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
    
    return render_template("dash/index.html", data=data, username=username)
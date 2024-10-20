from flask import Blueprint, redirect, render_template, request, url_for
import jwt, os

from app.dss.services import DssService
from middleware.auth import is_authenticated
from app.tourist.services import AttractionsService

tourist_bp = Blueprint('tourist', __name__, root_path="/tourist")


@tourist_bp.route('/tourist/attractions', methods=['GET'])
@is_authenticated
def attractions():
    token = request.cookies.get('token')
    attractions = AttractionsService.get_attractions()
    weight = DssService.get_weight()
    print(weight)

    # GET USERNAME
    if not token:
        return redirect(url_for('accounts.signin'))
    try:
        decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        username_data = {"username": decoded_token.get('username')} 
    except jwt.ExpiredSignatureError:
        return redirect(url_for('accounts.signin'))
    except jwt.InvalidTokenError:
        return redirect(url_for('accounts.signin'))
    
    data = {
        "attractions": attractions,
        "weight": weight,
    }
    
    return render_template("tourist/attractions.html", **data, username=username_data)
from flask import Blueprint, render_template, request
import jwt, os
from middleware.auth import is_authenticated
from app.tourist.services import AttractionsService

tourist_bp = Blueprint('tourist', __name__, root_path="/tourist")


@tourist_bp.route('/tourist/attractions', methods=['GET'])
@is_authenticated
def attractions():
    token = request.cookies.get('token')
    attractions = AttractionsService.get_attractions()
    data = {
        "attractions": attractions
    }
    return render_template("tourist/attractions.html", **data)
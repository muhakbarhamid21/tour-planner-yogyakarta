from urllib import request

from app.dss.services import DssService
from app.tourist.services import AttractionsService
from middleware.auth import is_authenticated
from flask import render_template, request, url_for, redirect
from flask.blueprints import Blueprint

dss_bp = Blueprint('dss', __name__, root_path="/dss")


@dss_bp.route('/dss/weight', methods=['GET', 'POST'])
@is_authenticated
def weight():
    if request.method == "POST":
        data = {}
        print("form request", request.form)
        return redirect(url_for("dss.analysis"))

    weight = DssService.get_weight()
    categories = AttractionsService.get_attraction_categories()

    data = {
        "weight": weight,
        "categories": categories
    }
    return render_template("dss/weight/index.html", **data)


@dss_bp.route('/dss/analysis', methods=['GET', 'POST'])
@is_authenticated
def analysis():
    data = {}
    return render_template("dss/analysis/index.html", **data)


@dss_bp.route('/dss/alternative', methods=['GET', 'POST'])
@is_authenticated
def alternative():
    data = {}
    return render_template("dss/analysis/index.html", **data)


@dss_bp.route('/dss/criteria', methods=['GET', 'POST'])
@is_authenticated
def criteria():
    data = {}
    return render_template("dss/analysis/index.html", **data)
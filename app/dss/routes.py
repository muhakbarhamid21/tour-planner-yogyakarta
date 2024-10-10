from urllib import request

from app.dss.services import DssService
from app.tourist.services import AttractionsService
from middleware.auth import is_authenticated
from flask import render_template, request, url_for, redirect
from flask.blueprints import Blueprint
from utils.topsis import TOPSISWithSubCriteria

dss_bp = Blueprint('dss', __name__, root_path="/dss")


@dss_bp.route('/dss/weight', methods=['GET', 'POST'])
@is_authenticated
def weight():
    if request.method == "POST":
        DssService.update_weight()
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
    categories = AttractionsService.get_attraction_categories()
    weight = DssService.get_weight()

    print("weight", weight)

    # topsis_model = TOPSISWithSubCriteria(data, sub_criteria_weights, criteria_weights, criteria_types)

    topsis = {
        "rank": [],
    }

    data = {
        "categories": categories,
        "weight": weight,
        "topsis": topsis
    }

    if request.method == "POST":
        category_id = request.form['category']
        preferences, rankings, alternative_labels = DssService.get_topsis(category_id=category_id)

        for i in range(len(preferences)):
            data["topsis"]["rank"].append({
                'alternative': alternative_labels[rankings[i]],
                'attraction': preferences[rankings[i]],
                'rank': i + 1
            })

        return render_template("dss/analysis/index.html", **data)

    return render_template("dss/analysis/index.html", **data)


@dss_bp.route('/dss/alternative', methods=['GET', 'POST'])
@is_authenticated
def alternative():
    data = {}
    return render_template("dss/alternative.html", **data)


@dss_bp.route('/dss/criteria', methods=['GET', 'POST'])
@is_authenticated
def criteria():
    criteria = DssService.get_criteria()
    data = {
        "criteria": criteria
    }

    if request.method == "POST":
        # print(request.form)
        DssService.update_criteria()
        return redirect(url_for("dss.criteria"))

    return render_template("dss/criteria.html", **data)
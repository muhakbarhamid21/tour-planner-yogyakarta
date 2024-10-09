from urllib import request
from middleware.auth import is_authenticated
from flask import render_template
from flask.blueprints import Blueprint

dss_bp = Blueprint('dss', __name__, root_path="/dss")


@dss_bp.route('/dss/weight', methods=['GET', 'POST'])
@is_authenticated
def weight():
    data = {}
    return render_template("dss/weight/index.html", **data)

@dss_bp.route('/dss/analysis', methods=['GET', 'POST'])
@is_authenticated
def analysis():
    data = {}
    return render_template("dss/analysis/index.html", **data)
# Define routes for User pages

from flask import Blueprint, render_template

user_bp = Blueprint('_user', __name__)

@user_bp.route('/user/dashboard-user')
def dashboard_user():
    return render_template('_user/dashboard-user.html')

@user_bp.route('/user/tourist-attractions-user')
def tourist_attractions_user():
    return render_template('_user/tourist-attractions-user.html')

@user_bp.route('/user/distance-generator-user')
def distance_generator_user():
    return render_template('_user/distance-generator-user.html')

@user_bp.route('/user/weighting-user')
def weighting_user():
    return render_template('_user/weighting-user.html')

@user_bp.route('/user/analysis-user')
def analysis_user():
    return render_template('_user/analysis-user.html')

@user_bp.route('/user/results-user')
def results_user():
    return render_template('_user/results-_user.html')

@user_bp.route('/user/alternative-user')
def alternative_user():
    return render_template('_user/alternative-user.html')

@user_bp.route('/user/parameter-user')
def parameter_user():
    return render_template('_user/parameter-user.html')

@user_bp.route('/user/criteria-user')
def criteria():
    return render_template('_user/criteria-user.html')
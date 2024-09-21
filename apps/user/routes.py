# Define routes for User pages

from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/dashboard-user')
def dashboard_user():
    return render_template('user/dashboard-user.html')

@user_bp.route('/user/tourist-attractions-user')
def tourist_attractions_user():
    return render_template('user/tourist-attractions-user.html')

@user_bp.route('/user/distance-generator-user')
def distance_generator_user():
    return render_template('user/distance-generator-user.html')

@user_bp.route('/user/weighting-user')
def weighting_user():
    return render_template('user/weighting-user.html')

@user_bp.route('/user/analysis-user')
def analysis_user():
    return render_template('user/analysis-user.html')

@user_bp.route('/user/results-user')
def results_user():
    return render_template('user/results-user.html')

@user_bp.route('/user/alternative-user')
def alternative_user():
    return render_template('user/alternative-user.html')

@user_bp.route('/user/parameter-user')
def parameter_user():
    return render_template('user/parameter-user.html')

@user_bp.route('/user/weight-user')
def weight_user():
    return render_template('user/weight-user.html')
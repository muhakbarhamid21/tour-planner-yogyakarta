from flask import Blueprint, render_template

guest_bp = Blueprint('_guest', __name__)

@guest_bp.route('/guest/dashboard-guest')
def dashboard_guest():
    return render_template('_guest/dashboard-guest.html')

@guest_bp.route('/guest/tourist-attractions-guest')
def tourist_attractions_guest():
    return render_template('_guest/tourist-attractions-guest.html')

@guest_bp.route('/guest/weighting-guest')
def weighting_guest():
    return render_template('_guest/weighting-guest.html')

@guest_bp.route('/guest/analysis-guest')
def analysis_guest():
    return render_template('_guest/analysis-guest.html')

@guest_bp.route('/guest/results-guest')
def results_guest():
    return render_template('_guest/results-_guest.html')
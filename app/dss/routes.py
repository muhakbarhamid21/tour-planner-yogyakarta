import os
from urllib import request

import jwt

from app.dss.services import DssService
from app.models import Attraction
from app.tourist.services import AttractionsService
from middleware.auth import is_authenticated
from flask import flash, jsonify, render_template, request, url_for, redirect, session
from flask.blueprints import Blueprint
from utils.jwt import decode_jwt
from utils.topsis import TOPSISWithSubCriteria

from flask_sqlalchemy import SQLAlchemy
from core.database import db

dss_bp = Blueprint('dss', __name__, root_path="/dss")


@dss_bp.route('/dss/weight', methods=['GET', 'POST'])
@is_authenticated
def weight():
    token = request.cookies.get('token')
    
    if request.method == "POST":
        DssService.update_weight()
        return redirect(url_for("dss.analysis"))

    weight = DssService.get_weight()
    categories = AttractionsService.get_attraction_categories()

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
        "weight": weight,
        "categories": categories,
        "username": username_data,
    }
    
    return render_template("dss/weight/index.html", **data)


@dss_bp.route('/dss/analysis', methods=['GET', 'POST'])
@is_authenticated
def analysis():
    token = request.cookies.get('token')
    
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
    
    categories = AttractionsService.get_attraction_categories()
    weight = DssService.get_weight()

    topsis = {
        "rank": [],
    }

    data = {
        "categories": categories,
        "weight": weight,
        "topsis": topsis,
        "username": username_data
    }

    if request.method == "POST":
        category_id = request.form['category']
        topsis, preferences, rankings, alternative_labels = DssService.get_topsis(category_id=category_id)

        if category_id != "all":
            attractions = AttractionsService.get_attractions(category_id=category_id)
        else:
            attractions = AttractionsService.get_attractions()

        for i in range(len(preferences)):
            data["topsis"]["rank"].append({
                'alternative': alternative_labels[rankings[i]],
                'attraction': preferences[rankings[i]],
                'rank': i + 1
            })
        data["attractions"] = attractions
        data["topsis"]["aggregated_data"] = topsis.aggregated_data
        data["topsis"]["norm_data"] = topsis.norm_data
        data["topsis"]["criteria_weights"] = topsis.criteria_weights
        data["topsis"]["weighted_data"] = topsis.weighted_data
        data["topsis"]["solution"] = {
            "ideal_best": topsis.ideal_best,
            "ideal_worst": topsis.ideal_worst
        }
        data["topsis"]["distance"] = {
            "dist_ideal_best": topsis.dist_to_ideal_best,
            "dist_ideal_worst": topsis.dist_to_ideal_worst
        }
        data["topsis"]["preferences"] = topsis.prefereces

        return render_template("dss/analysis/index.html", **data)

    return render_template("dss/analysis/index.html", **data)


@dss_bp.route('/dss/alternative', methods=['GET', 'POST', "DELETE"])
@is_authenticated
def alternative():
    data = {}

    token = request.cookies.get('token')

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

    data["username"] = username_data 

    if request.method == 'POST':
        attraction_id = request.form.get('attraction_id')  # Get attraction ID from the form if exists
        category_id = request.form.get('category_id')
        attraction_name = request.form.get('attraction')
        lon = request.form.get('lon')
        lat = request.form.get('lat')
        entry_price = request.form.get('entry_price')
        stars = request.form.get('stars')
        reviews = request.form.get('reviews')
        facility = request.form.get('facility')

        # Ensure all required fields are provided
        if not (category_id and attraction_name and lon and lat and entry_price and stars and reviews and facility):
            flash('Please fill out all fields', 'error')
            return redirect(url_for('dss.alternative'))

        # Get user_id from session or JWT
        jwt_data = decode_jwt()
        user_id = jwt_data.get("id")

        if attraction_id:  # If there's an attraction ID, it's an update
            return update_attraction(attraction_id, category_id, attraction_name, lon, lat, entry_price, stars, reviews, facility)
        else:  # Otherwise, it's a new add
            return add_attraction(category_id, attraction_name, lon, lat, entry_price, stars, reviews, facility, user_id)

    attractions_by_category = AttractionsService.get_attractions_by_category()
    data['attractions_by_category'] = attractions_by_category

    return render_template("dss/alternative.html", **data)


# Function to add a new attraction
def add_attraction(category_id, attraction_name, lon, lat, entry_price, stars, reviews, facility, user_id):
    try:
        # Add new attraction
        AttractionsService.add_attraction(
            category_id=category_id,
            name=attraction_name,
            lon=lon,
            lat=lat,
            entry_price=entry_price,
            stars=stars,
            reviews=reviews,
            facility=facility,
            user_id=user_id
        )
        flash('Attraction added successfully!')
    except Exception as e:
        flash(f'Error adding attraction: {e}', 'error')
    return redirect(url_for('dss.alternative'))


# Function to update an existing attraction
def update_attraction(attraction_id, category_id, attraction_name, lon, lat, entry_price, stars, reviews, facility):
    try:
        attraction = Attraction.query.get(attraction_id)
        if attraction:
            # Update the attraction fields
            attraction.category_id = category_id
            attraction.name = attraction_name
            attraction.lon = lon
            attraction.lat = lat
            attraction.entry_price = entry_price
            attraction.stars = stars
            attraction.reviews = reviews
            attraction.facility = facility

            db.session.commit()
            flash('Attraction updated successfully!')
        else:
            flash('Attraction not found!', 'error')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating attraction: {e}', 'error')
    
    return redirect(url_for('dss.alternative'))

@dss_bp.route('/dss/alternative/delete/<int:id>', methods=['DELETE'])
@is_authenticated
def delete_attraction(id):
    # Mencari data berdasarkan ID
    attraction = Attraction.query.get(id)

    if attraction:
        try:
            # Merge objek dengan sesi aktif sebelum menghapus
            attraction = db.session.merge(attraction)
            db.session.delete(attraction)
            db.session.commit()
            print("Atraksi berhasil dihapus")
            return jsonify({"message": "Atraksi berhasil dihapus"}), 204
        except Exception as e:
            db.session.rollback()
            print(f"Kesalahan saat menghapus atraksi: {e}")
            return jsonify({"message": f"Gagal menghapus atraksi. Error: {str(e)}"}), 500
    else:
        print("Atraksi tidak ditemukan")
        return jsonify({"message": "Atraksi tidak ditemukan"}), 404


@dss_bp.route('/dss/criteria', methods=['GET', 'POST'])
@is_authenticated
def criteria():
    token = request.cookies.get('token')

    # Validasi token dan ambil username
    if not token:
        return redirect(url_for('accounts.signin'))
    try:
        decoded_token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        username_data = {"username": decoded_token.get('username')}  # Simpan username dalam dictionary
    except jwt.ExpiredSignatureError:
        return redirect(url_for('accounts.signin'))  # Token expired, redirect ke login
    except jwt.InvalidTokenError:
        return redirect(url_for('accounts.signin'))
    
    
    criteria = DssService.get_criteria()
    data = {
        "criteria": criteria,
        "username": username_data
    }

    if request.method == "POST":
        # print(request.form)
        DssService.update_criteria()
        return redirect(url_for("dss.criteria"))

    return render_template("dss/criteria.html", **data)
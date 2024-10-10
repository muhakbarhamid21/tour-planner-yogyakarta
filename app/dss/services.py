from app.tourist.services import AttractionsService
from middleware.auth import is_authenticated
from utils.jwt import decode_jwt
from utils.topsis import TOPSISWithSubCriteria
from sqlalchemy import text
from core.database import db
from flask import flash, request
from app.models import Attraction, Weight, Criteria

import numpy as np


class DssService:

    def __init__(self):
        pass

    @staticmethod
    def get_topsis(category_id):
        if category_id != 'all':
            attraction = AttractionsService.get_attractions(category_id)
        else:
            attraction = AttractionsService.get_attractions()

        columns = ["name", "entry_price", "facility", "stars", "reviews", "distance"]

        # Mengambil data berdasarkan key dalam columns untuk setiap dictionary di list
        data = [{key: item[key] for key in columns if key in item} for item in attraction]

        primary_weight = DssService.get_weight()

        # weight_col = ["entry_price", "facility", "rating", "distance"]
        criteria_weights = {
            "entry_price": primary_weight["entry_price"] / 100,
            "facility": primary_weight["facility"] / 100,
            "rating": primary_weight["rating"]["value"] / 100,
            "distance": primary_weight["distance"] / 100
        }

        # sub_weight_col = ["rating.stars". "rating.reviews"]
        sub_criteria_weights = {
            "rating": {
                "stars": primary_weight["rating"]["stars"] / 100,
                "reviews": primary_weight["rating"]["reviews"] / 100
            }
        }

        criteria_types = DssService.get_criteria_topsis()

        topsis = TOPSISWithSubCriteria(
            data, sub_criteria_weights, criteria_weights, criteria_types
        )
        preferences, rankings, alternative_labels = topsis.rank()

        # print(preferences)
        # print(rankings)
        # print(alternative_labels)

        return topsis, preferences, rankings, alternative_labels

    @staticmethod
    def get_criteria_topsis():
        sql_query = text("""SELECT * FROM dss_criteria""")
        results = db.session.execute(sql_query).fetchall()

        criteria = {}
        for row in results:
            criteria.update({row.key: row.criteria})

        db.session.close()

        return criteria

    @staticmethod
    def get_criteria():
        sql_query = text("""SELECT * FROM dss_criteria""")
        results = db.session.execute(sql_query).fetchall()

        criteria = [{
            "id": row.id,
            "name": row.name,
            "criteria": row.criteria,
            "key": row.key
        } for row in results]
        db.session.close()

        return criteria

    @staticmethod
    def update_criteria():
        criteria_id = request.form['criteria_id']
        criteria = request.form['criteria']

        data = Criteria.query.filter_by(id=criteria_id).first()

        if data:
            # Jika data ada, lakukan update
            data.criteria = criteria
            flash('Weights updated successfully!')

        # Commit perubahan ke database
        db.session.commit()
        db.session.close()

        return True

    @staticmethod
    def update_weight():
        # Simulasi mendapatkan user_id dari session atau form
        distance = request.form['distance']
        entry_price = request.form['entry_price']
        rating = request.form['rating']
        stars = request.form['stars']
        reviews = request.form['reviews']
        facility = request.form['facility']

        jwt_data = decode_jwt()

        # Cari data Weight berdasarkan user_id
        weight = Weight.query.filter_by(user_id=jwt_data.get("id")).first()

        if weight:
            # Jika data ada, lakukan update
            weight.distance = distance
            weight.entry_price = entry_price
            weight.rating = rating
            weight.stars = stars
            weight.reviews = reviews
            weight.facility = facility
            flash('Weights updated successfully!')
        else:
            # Jika data tidak ada, buat data baru
            new_weight = Weight(
                user_id=jwt_data.get("id"),
                distance=distance,
                entry_price=entry_price,
                rating=rating,
                stars=stars,
                reviews=reviews,
                facility=facility
            )
            db.session.add(new_weight)
            flash('Weights created successfully!')

        # Commit perubahan ke database
        db.session.commit()
        db.session.close()

        return True


    @staticmethod
    @is_authenticated
    def get_weight():
        jwt_data = decode_jwt()

        query = text(f"""SELECT 
            id,
            distance,
            entry_price,
            facility,
            rating,
            stars,
            reviews
        FROM dss_weights WHERE user_id = {jwt_data['id']}""")
        result = db.session.execute(query).fetchone()

        if result:
            weight = {
                "id": result[0],
                "distance": result[1],
                "entry_price": result[2],
                "facility": result[3],
                "rating": {
                    "value": result[4],
                    "stars": result[5],
                    "reviews": result[6]
                },
            }
        else:
            weight = {
                "id": None,
                "distance": 0,
                "entry_price": 0,
                "facility": 0,
                "rating": {
                    "value": 0,
                    "stars": 0,
                    "reviews": 0
                },
            }

        return weight

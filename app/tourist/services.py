from flask import flash
from app.models import Attraction
from core.database import db
from sqlalchemy import text
from utils.location import haversine


class AttractionsService:

    def __init__(self):
        pass
    
    def get_attraction_categories():
        sql_query = text("""SELECT
         id, name
        FROM tourist_attraction_categories""")

        results = db.session.execute(sql_query).fetchall()

        categories = [{
            "id": row.id,
            "name": row.name
        } for row in results]

        return categories

    @staticmethod
    def get_attractions(category_id = None):
        user_lat = -7.7669578
        user_lon = 110.3714613

        if category_id:
            # filter by id
            sql_query = text(f"""SELECT
                ta.id, 
                ta.name, 
                ta.entry_price, 
                ta.facility,
                ta.stars,
                ta.reviews,
                ta.lat,
                ta.lon,
                ta.created_at,
                ta.user_id,
                tac.id AS Category_id,
                tac.name AS category
            FROM tourist_attractions ta 
            JOIN tourist_attraction_categories tac 
            ON ta.category_id = tac.id
            WHERE ta.category_id = {category_id}""")
        else:
            sql_query = text("""SELECT
                ta.id, 
                ta.name, 
                ta.entry_price, 
                ta.facility,
                ta.stars,
                ta.reviews,
                ta.lat,
                ta.lon,
                ta.created_at,
                ta.user_id,
                tac.id AS Category_id,
                tac.name AS category
            FROM tourist_attractions ta 
            JOIN tourist_attraction_categories tac 
            ON ta.category_id = tac.id""")

        # Eksekusi query SQL
        result = db.session.execute(sql_query).fetchall()

        # Mengonversi hasil query ke format JSON yang diinginkan
        attractions = [
            {
                "id": row.id,
                "name": row.name,
                "entry_price": row.entry_price,
                "facility": row.facility,
                "stars": row.stars,
                "reviews": row.reviews,
                "created_at": row.created_at,
                "user_id": row.user_id,
                "lat": row.lat,
                "lon": row.lon,
                "category": {
                    "id": row.category_id,
                    "name": row.category
                }
            }
            for row in result
        ]

        # Menghitung jarak untuk setiap objek attraction
        for attraction in attractions:
            attraction['distance'] = haversine(user_lon, user_lat, attraction['lon'], attraction['lat'])

        return attractions
    
    @staticmethod
    def get_attractions_by_category():
        attractions = AttractionsService.get_attractions()
        
        category_1 = [attr for attr in attractions if attr['category']['id'] == 1]
        category_2 = [attr for attr in attractions if attr['category']['id'] == 2]
        category_3 = [attr for attr in attractions if attr['category']['id'] == 3]
        category_4 = [attr for attr in attractions if attr['category']['id'] == 4]
        
        attractions_by_category = {
            "category_1": category_1,
            "category_2": category_2,
            "category_3": category_3,
            "category_4": category_4
        }
        
        return attractions_by_category
    
    @staticmethod
    def add_attraction(category_id, name, lon, lat, entry_price, stars, reviews, facility, user_id):
        new_attraction = Attraction(
            category_id=category_id,
            name=name,
            lon=lon,
            lat=lat,
            entry_price=entry_price,
            stars=stars,
            reviews=reviews,
            facility=facility,
            user_id=user_id
        )

        try:
            db.session.add(new_attraction)
            db.session.commit()
            flash('Attraction added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding attraction: {e}', 'error')

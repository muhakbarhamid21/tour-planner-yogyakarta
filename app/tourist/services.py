from app.models import Attraction
from core.database import db
from sqlalchemy import text

def get_attractions():
    # Menjalankan query SQL langsung menggunakan connection object dari db
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

    return attractions
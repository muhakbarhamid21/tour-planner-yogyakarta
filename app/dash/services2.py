from sqlalchemy import text
from core.database import db

# Fungsi untuk mendapatkan jumlah wisata berdasarkan category_id tertentu
def get_attraction_count_for_category(category_id):
    sql_query = text("""
        SELECT COUNT(*) 
        FROM tourist_attractions 
        WHERE category_id = :category_id
    """)
    result = db.session.execute(sql_query, {"category_id": category_id}).scalar()
    return result
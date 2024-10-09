from sqlalchemy import text
from core.database import db

def get_attraction_counts():
    counts = {}

    categories = [1, 2, 3, 4] 
    for category_id in categories:
        sql_query = text(f"""
            SELECT COUNT(*) 
            FROM tourist_attractions 
            WHERE category_id = :category_id
        """)
        result = db.session.execute(sql_query, {"category_id": category_id}).scalar()
        counts[category_id] = result

    return counts
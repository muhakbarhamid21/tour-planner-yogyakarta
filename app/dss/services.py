from middleware.auth import is_authenticated
from utils.jwt import decode_jwt
from sqlalchemy import text
from core.database import db


class DssService:

    def __init__(self):
        pass


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
            reviews,
            attraction_type
        FROM dss_weights WHERE user_id = {jwt_data['id']}""")
        result = db.session.execute(query).fetchone()

        if result:
            weight = {
                "id": result[0],
                "distance": result[1],
                "entry_price": result[2],
                "facility": result[3],
                "attraction_type": result[7],
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

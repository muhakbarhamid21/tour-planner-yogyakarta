from sqlalchemy import text
from core.database import db


class AdminService:

    @staticmethod
    def get_users():
        query_sql = text("""SELECT id, email, username, fullname, created_at FROM account_users""")
        results = db.session.execute(query_sql).fetchall()
        print(results)
        users = [{
            "id": row.id,
            "email": row.email,
            "username": row.username,
            "fullname": row.fullname,
            "created_at": row.created_at
        } for row in results]

        return users


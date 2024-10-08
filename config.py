import os

SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')

# Komponen URI PostgreSQL
DB_USER = os.getenv('DB_USER', 'default_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'default_password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'my_database')

# SQLAlchemy Database URI untuk PostgreSQL
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Disable modification tracking to avoid overhead
SQLALCHEMY_TRACK_MODIFICATIONS = False

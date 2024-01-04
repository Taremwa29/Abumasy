# config.py
from urllib.parse import quote_plus

class Config:
    password = "Atgtblsd5@1311"
    quoted_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{quoted_password}@127.0.0.1:3306/abumasy"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


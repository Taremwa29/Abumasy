# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
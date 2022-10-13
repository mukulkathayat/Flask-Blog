import os

class Config:
    SECRET_KEY = os.environ.get('FB_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FB_DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_POST = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

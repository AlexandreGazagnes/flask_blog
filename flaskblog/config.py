import os


class Config():
    """config info for app"""

    SECRET_KEY = os.environ.get('SECRET_KEY_FLASK_BLOG')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI_FLASK_BLOG')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 'smtp.googlemail.com'
    MAIL_USERNAME = os.environ.get("SERVER_EMAIL_FLASK_BLOG")
    MAIL_PASSWORD = os.environ.get("SERVER_PASSWORD_FLASK_BLOG")

import os

class Config:
    """Parent class for general configurations settings"""
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Elm1n10@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
    """
    Config Child class for Production configurations 
    Args:
        Config : Parent configurations settings to be inherited
    """
    
    pass

class DevConfig(Config):
    """
    Config child class for Development configuration

    Args:
        Config : Parent configurations settings to be inherited
    """
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
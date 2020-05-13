import os

class Config:
    '''
    General configuration parent class
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.urandom(69)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nairdaee:mutemuas2001@localhost/blogs'
class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    def init_app(app):
        pass

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nairdaee:mutemuas2001@localhost/blogs'
    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig,
'test':TestConfig
}

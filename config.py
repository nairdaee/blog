import os

class Config
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.random(69)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nairdaee:mutemuas2001@localhost/blog'
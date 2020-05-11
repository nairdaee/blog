from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)


     #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
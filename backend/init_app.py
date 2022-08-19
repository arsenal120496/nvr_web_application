from routes.camera import camera_page
from routes.record import record_page
from routes.user import user_page
# from routes.user import user_page
import logging
from logging.handlers import RotatingFileHandler
def set_config(app):
    # setting which configuration to use depending on the environment
    if app.config["ENV"] == "production":
        app.config.from_object('configs.config.ProductionConfig')
    elif app.config["ENV"] == "testing":
        app.config.from_object('configs.config.TestingConfig')
    elif app.config["ENV"] == "development":
        app.config.from_object('configs.config.DevelopmentConfig')

def init_db(app):
    # initialize the database and setup models
    from app import db  
    from models import Camera, Record, User
    from models import Camera
    from models import Record
    # from models import User
    db.init_app(app)
    with app.app_context():
        db.create_all()

def init_blueprint(app):
    # set up Flask routes to manipulate the database
    with app.app_context():
        app.register_blueprint(camera_page, url_prefix='/camera')
        app.register_blueprint(record_page, url_prefix='/record')
        # app.register_blueprint(user_page, url_prefix='/user')

def config_log(app):
    # setup logging config file for service files tracking history
    # maximum number of files is 10, each file is 5MB maximum
    logging.basicConfig(
        handlers=[RotatingFileHandler('record.log', maxBytes=5*1024, backupCount=10)],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",    
        datefmt='%Y-%m-%dT%H:%M:%S')
    return "initializing logging levels"

def config_log(app):
    # setup logging config file for service files tracking history
    # maximum number of files is 10, each file is 5MB maximum
    logging.basicConfig(
        handlers=[RotatingFileHandler('record.log', maxBytes=5*1024, backupCount=10)],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",    
        datefmt='%Y-%m-%dT%H:%M:%S')
    return "initializing logging levels"


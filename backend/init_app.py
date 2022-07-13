from routes.camera import camera_page
from routes.record import record_page

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
    from models import Camera
    from models import Record
    db.init_app(app)
    with app.app_context():
        db.create_all()

def init_blueprint(app):
    # set up Flask routes to manipulate the database
    with app.app_context():
        app.register_blueprint(camera_page, url_prefix='/camera')
        app.register_blueprint(record_page, url_prefix='/record')


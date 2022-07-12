from flask_sqlalchemy import SQLAlchemy
from routes.camera import camera_page
from routes.manager import manager_page
from flask_migrate import Migrate

def set_config(app):
    # setting which configuration to use depending on the environment
    if app.config["ENV"] == "production":
        app.config.from_object('configs.config.ProductionConfig')
    elif app.config["ENV"] == "testing":
        app.config.from_object('configs.config.TestingConfig')
    elif app.config["ENV"] == "development":
        app.config.from_object('configs.config.DevelopmentConfig')

def init_db(app):
    migrate = Migrate()
    db = SQLAlchemy(app)
    db.init_app(app)
    migrate.init_app(app,db)

    # em có thử cách define luôn camera model trong này nó vẫn chạy 
    # nhưng không tách ra 2 thằng model riêng trong 2 file ở folder model

    return db

def init_blueprint(app):
    with app.app_context():
        app.register_blueprint(camera_page, url_prefix='/camera')
        app.register_blueprint(manager_page, url_prefix='/manager')



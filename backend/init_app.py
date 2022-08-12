from routes.camera import camera_page
from routes.record import record_page
from routes.user import user_page

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
    db.init_app(app)
    with app.app_context():
        db.create_all()

def init_blueprint(app):
    # set up Flask routes to manipulate the database
    with app.app_context():
        app.register_blueprint(camera_page, url_prefix='/camera')
        app.register_blueprint(record_page, url_prefix='/record')
        app.register_blueprint(user_page, url_prefix='/user')

class CameraObject:
    def __init__(self):
        self.queue = [20]
    
    def update_frame(self, frame):
        print("update frame")
        if len(self.queue) > 20:
            self.queue.pop(0) 
        self.queue.append(frame)
    
    def get_frame(self):
        return self.queue[0]


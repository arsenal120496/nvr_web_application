from flask import Flask
from routes.routes import simple_page
from flask_cors import CORS
from models.shared_model import db

app = Flask(__name__)

# setting which configuration to use depending on the environment
if app.config["ENV"] == "production":
    app.config.from_object('configs.config.ProductionConfig')
elif app.config["ENV"] == "testing":
    app.config.from_object('configs.config.TestingConfig')
elif app.config["ENV"] == "development":
    app.config.from_object('configs.config.DevelopmentConfig')

# Creating sqlite database and connecting blueprint routes
db.app = app
db.init_app(app)
app.register_blueprint(simple_page)

# prevent CORS 
CORS(app)

db.create_all()
if __name__ == "__main__":
    app.run(debug=True)







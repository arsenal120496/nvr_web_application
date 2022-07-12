from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from init_app import init_db, init_blueprint, set_config
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_migrate import Migrate



app = Flask(__name__)
app.config["ENV"] = "development"
# Creating sqlite database and connecting blueprint routes
set_config(app)
# prevent CORS 
CORS(app)
db = SQLAlchemy()
migrate = Migrate()
init_db(app)
init_blueprint(app)

if __name__ == "__main__":
    app.run(debug=True)
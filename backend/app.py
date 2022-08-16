from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from init_app import init_db, init_blueprint, set_config, config_log
from flask_migrate import Migrate
from flask_migrate import Migrate
from logging.config import fileConfig

app = Flask(__name__)
# set the configuration for the application
app.config["ENV"] = "development"
set_config(app)
config_log(app)
# prevent CORS
CORS(app)

# set up the database and model
db = SQLAlchemy()
migrate = Migrate()
init_db(app)

# set up the blueprint for routes that manipulate the database 
init_blueprint(app)

if __name__ == "__main__":
    app.run(debug=True)







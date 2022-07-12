from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from init_app import init_db, init_blueprint,set_config

app = Flask(__name__)
# Creating sqlite database and connecting blueprint routes
set_config(app)
# prevent CORS 
CORS(app)

db = init_db(app)


# model bắt buộc phải để ngay đây sau thằng init_db (em tìm cách define model trong file model
# rồi import vô đây nhưng không được)

# khi chạy thì mình sẽ ra database.db có chứa 2 table là Camera và Manager
class Camera(db.Model):
    pass
class Manager(db.Model):
    pass

init_blueprint(app)

db.create_all()
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
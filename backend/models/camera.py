from app import db 

# model này đang được define và sử dụng trong app.py

class Camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.String(240))
    status = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, camera_name, status):
        self.camera_name = camera_name
        self.status = status
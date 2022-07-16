from app import db 
class Camera(db.Model):
    camera_id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.String(240))
    rtsp_link = db.Column(db.String(240))

    def __init__(self, camera_name, rtsp_link):
        self.camera_name = camera_name
        self.rtsp_link = rtsp_link
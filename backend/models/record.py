from app import db
class Record(db.Model):
    camera_id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.String(240))
    rtsp_url = db.Column(db.String(240))

    def __init__(self, camera_name, rtsp_url):
        self.camera_name = camera_name
        self.rtsp_url = rtsp_url
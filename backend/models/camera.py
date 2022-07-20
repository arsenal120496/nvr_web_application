from requests import request
from app import db
from flask import jsonify
from flask_api import status
class Camera(db.Model):
    camera_id = db.Column(db.Integer, primary_key=True)
    camera_name = db.Column(db.String(240))
    rtsp_url = db.Column(db.String(240))

    def __init__(self, camera_name, rtsp_url):
        self.camera_name = camera_name
        self.rtsp_url = rtsp_url
        
    def create(name, url):
        return Camera(camera_name= name, rtsp_url=url)
    
    def retrieveList():
        return Camera.query.all()

    def retrieveCamera(id):
        try: 
            query_item = Camera.query.get(id)
        except:
            return jsonify({"message": "queried camera not existed"}), status.HTTP_404_NOT_FOUND
        return query_item
    
    def update(id):
        try:
            update_item = Camera.query.get(id).first()
            db.session.delete(update_item)
            db.session.commit()
            camera_name = request.json['camera_name']
            rtsp_url = request.json['rtsp_url']
            new_item = Camera(camera_id=id, camera_name=camera_name, rtsp_url=rtsp_url)

            db.session.add(new_item)
            db.session.commit()
            return new_item
        except:
            return jsonify({"message": "queried camera not existed"}), status.HTTP_404_NOT_FOUND

    def delete(id):
        try: 
            delete_item = Camera.query.filter_by(camera_id=id).first()
            db.session.delete(delete_item)
            db.session.commit()
            return jsonify({"message": "camera deleted successfully"})

        except:
            return jsonify({"message": "queried camera not existed"}), status.HTTP_404_NOT_FOUND



    


    
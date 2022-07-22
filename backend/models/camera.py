from requests import request
from app import db
from flask import Response, jsonify
from flask_api import status
from sqlalchemy.inspection import inspect


class Camera(db.Model):
    camera_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    camera_name = db.Column(db.String(240), unique= True, nullable=False)
    rtsp_url = db.Column(db.String(240),unique=True, nullable=False)

    def __init__(self, user_id, camera_name, rtsp_url):
        self.user_id = user_id 
        self.camera_name = camera_name
        self.rtsp_url = rtsp_url
        
    def retrieveList():
        all_camera = Camera.query.all()
        camera_list = []
        for i in range(len(all_camera)):
            camera_dictionary = all_camera[i].toDict()
            camera_list.append(camera_dictionary)
        # thằng này return status 200 là nó bị cái lỗi giống hôm qua em cho anh coi
        return camera_list

    def retrieveCamera(id):
        try: 
            query_item = Camera.query.get(id)
            query_dictionary = Camera.toDict(query_item)
            # thằng này return status 200 là nó bị cái lỗi giống hôm qua em cho anh coi
            return query_dictionary
        except:
            return Response(jsonify({"message": "queried camera not existed"}), status=404, mimetype='application/json')
    
    def update(id):
        try:
            update_item = Camera.query.get(id).first()
            db.session.delete(update_item)
            db.session.commit()
            camera_name = request.json['camera_name']
            rtsp_url = request.json['rtsp_url']
            user_id = request.json['user_id']
            new_item = Camera(camera_id=id, user_id=user_id, camera_name=camera_name, rtsp_url=rtsp_url)
            db.session.add(new_item)
            db.session.commit()
            return new_item, status.HTTP_200_OK
        except:
            return Response(jsonify({"message": "queried camera not existed"}), status=404, mimetype='application/json')

    def delete(id):
        try: 
            delete_item = Camera.query.filter_by(camera_id=id).first()
            db.session.delete(delete_item)
            db.session.commit()
            return Response(jsonify({"message": "camera deleted successfully"}), status=200, mimetype='application/json')
        except:
            return Response(jsonify({"message": "queried camera not existed"}), status=404, mimetype='application/json')


    # convert a Camera object to dictionary
    def toDict(camera_object):
        try:
            converted_item = {}
            for field in [c.key for c in inspect(camera_object).mapper.column_attrs]:
                data = camera_object.__getattribute__(field)     
                converted_item[field] = data
            return converted_item
        except Exception as err:
            return Response(jsonify({"message": "error {}".format(err)}), status=404, mimetype='application/json')


    


    
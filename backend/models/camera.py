from app import db
from sqlalchemy.inspection import inspect
import logging
from database.database_manipulator import Database

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
        try: 
            all_camera = Camera.query.all()
            camera_list = []
            for i in range(len(all_camera)):
                camera_dictionary = all_camera[i].toDict()
                camera_list.append(camera_dictionary)
            logging.info("list of all cameras retrieved successfully")
            return camera_list
        except Exception as err:
            logging.warning("unable to retrieve list, error {}".format(err))
            return {"message": "error {}".format(err)}

    def retrieveCamera(id):
        try: 
            query_item = Camera.query.get(id)
            query_dictionary = Camera.toDict(query_item)
            logging.info("camera object retrieved successfully")
            return query_dictionary
        except Exception as err:
            logging.warning("unable to retrieve cammera object, error {}".format(err))
            return {"message": "error {}".format(err)}    

    def update(id, updating_item):
        try:
            object = Camera.query.get(id)
            object.user_id = updating_item['user_id']
            object.camera_name = updating_item['camera_name']
            object.rtsp_url = updating_item['rtsp_url']
            Database.save()
            logging.info("camera object updated successfully")
            return {"message": "item updated successfully"}
        except Exception as err:   
            logging.warning("unable to update camera object, err {}".format(err)) 
            return {"message": "error {}".format(err)}

    def delete(id):
        try: 
            delete_item = Camera.query.filter_by(camera_id=id).first()
            Database.delete(delete_item)        
            logging.info("camera object deleted successfully")
            return {"message": "camera deleted successfully"}
        except Exception as err:
            logging.warning("unable to delete camera object, err {}".format(err))
            return {"message": "error {}".format(err)}

    # convert a Camera object to dictionary, return empty dictionary if 
    def toDict(camera_object):
        try:
            converted_item = {}
            if camera_object is None:
                logging.info("camera object is NoneType")
                return {}
            else:
                for field in [c.key for c in inspect(camera_object).mapper.column_attrs]:
                    data = camera_object.__getattribute__(field)     
                    converted_item[field] = data
                logging.info("camera object converted to dictionary successfully")
                return converted_item
        except Exception as err: 
            logging.warning("unable to convert camera object to dictionary, err {}".format(err))
            return {"message": "error {}".format(err)}


    


    
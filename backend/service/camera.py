import logging
from database.database_manipulator import Database
import cv2
class CameraService:
    # function that adds the input object to the database
    def add_to_database(object):
        try: 
            Database.add(object)
            logging.info("camera added successfully")
        except Exception as err:
            logging.warning("fail to add camera object, err {}".format(err))

    # function that deletes the input object to the database
    def delete_from_database(object):
        try:
            from models import Camera
            item_id = object.camera_id
            delete_item = Camera.query.get(item_id)
            Database.delete(delete_item)
            logging.info("camera deleted successfully")
        except Exception as err:
            logging.warning("fail to delete camera object, err {}".format(err))
        
    # function that change the input object's camera name to target name
    def change_camera_name(object, target_name):
        try: 
            from models import Camera
            item_id = object.camera_id
            update_item = Camera.query.get(item_id)
            update_item.camera_name = target_name
            Database.save()
            logging.info("camera's name updated successfully")
        except Exception as err:
            logging.warning("fail to update camera's name, err{}".format(err))

    # function that change the input object's camera url to target url
    def change_camera_url(object, target_url):
        try: 
            from models import Camera
            item_id = object.camera_id
            update_url = Camera.query.get(item_id)
            update_url.rtsp_url = target_url
            Database.save()
            logging.info("camera's url updated successfully")
        except Exception as err:
            logging.warning("fail to update camera's url, err{}".format(err))

    # function that return the list of all camera objects currently in the database
    def get_database():
        try:
            from models import Camera
            camera_list = Camera.retrieveList()
            logging.info("database retrieved successfully")
            return camera_list
        except Exception as err:
            logging.warning("fail to retrieve database information, err{}".format(err))
            return {"message": "fail to retrieve database information, err {}".format(err)}

    # function that add the input camera object to database
    def add_camera_service(user_id, camera_name, rtsp_url):
        from models import Camera
        # check in case camera object passed in from front end is an empty object (NoneType)
        try:
            camera_to_add = Camera(user_id=user_id, camera_name=camera_name, rtsp_url=rtsp_url)
            # check the uniqueness of camera name and its rtsp url
            camera_name_count = Camera.query.filter_by(camera_name=camera_name).count()
            camera_url_count = Camera.query.filter_by(rtsp_url=rtsp_url).count()
            if camera_name_count == 0 and camera_url_count == 0:
                CameraService.add_to_database(camera_to_add)
                return {"message": "camera added successfully"}
            else: 
                logging.warning("camera already existed in the database")
                return {}
        except Exception as err:
            logging.warning("fail to add camera to database, err {}".format(err))
            return {"message": "fail to add camera to database, err {}".format(err)}
        

    # function that returns the information of the camera object based on input id 
    def query_camera_service(id):
        from models import Camera
        try: 
            query_camera = Camera.retrieveCamera(id)
            logging.info("camera queried successfully")
            return query_camera
        except Exception as err:
            logging.warning("fail to query camera's information, err {}".format(err))
            return {"message": "error {}".format(err)}

    def retrieve_rtmp(pipe):
        import numpy
        while True:
            raw_image = pipe.stdout.read(1280*720*3)
            image = numpy.fromstring(raw_image, dtype='uint8')
            image = image.reshape((720, 1280,3))
            ret, jpg = cv2.imencode(".jpg", image)
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + jpg.tobytes() + b"\r\n\r\n"
            )
            pipe.stdout.flush() 

    # function that adds the input object to the database
    def add_to_database(object):
        try: 
            Database.add(object)
            logging.info("camera added successfully")
        except Exception as err:
            logging.warning("fail to add camera object, err {}".format(err))

    # function that deletes the input object to the database
    def delete_from_database(object):
        try:
            from models import Camera
            item_id = object.camera_id
            delete_item = Camera.query.get(item_id)
            Database.delete(delete_item)
            logging.info("camera deleted successfully")
        except Exception as err:
            logging.warning("fail to delete camera object, err {}".format(err))
        
    # function that change the input object's camera name to target name
    def change_camera_name(object, target_name):
        try: 
            from models import Camera
            item_id = object.camera_id
            update_item = Camera.query.get(item_id)
            update_item.camera_name = target_name
            Database.save()
            logging.info("camera's name updated successfully")
        except Exception as err:
            logging.warning("fail to update camera's name, err{}".format(err))

    # function that change the input object's camera url to target url
    def change_camera_url(object, target_url):
        try: 
            from models import Camera
            item_id = object.camera_id
            update_url = Camera.query.get(item_id)
            update_url.rtsp_url = target_url
            Database.save()
            logging.info("camera's url updated successfully")
        except Exception as err:
            logging.warning("fail to update camera's url, err{}".format(err))

    # function that return the list of all camera objects currently in the database
    def get_database():
        try:
            from models import Camera
            camera_list = Camera.retrieveList()
            logging.info("database retrieved successfully")
            return camera_list
        except Exception as err:
            logging.warning("fail to retrieve database information, err{}".format(err))
            return {"message": "fail to retrieve database information, err {}".format(err)}

    # function that add the input camera object to database
    def add_camera_service(user_id, camera_name, rtsp_url):
        from models import Camera
        # check in case camera object passed in from front end is an empty object (NoneType)
        try:
            camera_to_add = Camera(user_id=user_id, camera_name=camera_name, rtsp_url=rtsp_url)
            # check the uniqueness of camera name and its rtsp url
            camera_name_count = Camera.query.filter_by(camera_name=camera_name).count()
            camera_url_count = Camera.query.filter_by(rtsp_url=rtsp_url).count()
            if camera_name_count == 0 and camera_url_count == 0:
                CameraService.add_to_database(camera_to_add)
                return {"message": "camera added successfully"}
            else: 
                logging.warning("camera already existed in the database")
                return {}
        except Exception as err:
            logging.warning("fail to add camera to database, err {}".format(err))
            return {"message": "fail to add camera to database, err {}".format(err)}
        

    # function that returns the information of the camera object based on input id 
    def query_camera_service(id):
        from models import Camera
        try: 
            query_camera = Camera.retrieveCamera(id)
            logging.info("camera queried successfully")
            return query_camera
        except Exception as err:
            logging.warning("fail to query camera's information, err {}".format(err))
            return {"message": "fail to query camera's information, err {}".format(err)}
    

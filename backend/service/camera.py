from sqlalchemy.inspection import inspect
from flask import jsonify
from flask_api import status

# function that adds the input object to the database
def add_to_database(object):
    from app import db
    db.session.add(object)
    db.session.commit()

# function that deletes the input object to the database
def delete_from_database(object):
    from app import db 
    from models import Camera
    item_id = object.camera_id
    delete_item = Camera.query.get_or_404(item_id)
    db.session.delete(delete_item)
    db.session.commit()

# function that change the input object's camera name to target name
def change_camera_name(object, target_name):
    from app import db
    from models import Camera
    item_id = object.camera_id
    update_item = Camera.query.get_or_404(item_id)
    update_item.camera_name = target_name
    db.session.commit()

# function that change the input object's camera url to target url
def change_camera_url(object, target_url):
    from app import db
    from models import Camera
    item_id = object.camera_id
    update_item = Camera.query.get_or_404(item_id)
    update_item.url = target_url
    db.session.commit()

# function that return the list of all camera objects currently in the database
def get_database():
    from models import Camera
    all_camera = Camera.query.all()
    camera_list = []
    for i in range(len(all_camera)):
        camera_dictionary = {}
        for field in [c.key for c in inspect(all_camera[i]).mapper.column_attrs]:
            data = all_camera[i].__getattribute__(field)
            camera_dictionary[field] = data
            camera_list.append(camera_dictionary)
    camera_list = list({(v['camera_name'], v['rtsp_url']):v for v in camera_list}.values())
    return camera_list

# function that add the input camera object to database
def add_camera_service(camera_object):
    from models import Camera
    # check in case camera object passed in from front end is an empty object (NoneType)
    try:
        camera_name = camera_object['camera_name']
        rtsp_url = camera_object['rtsp_url']
    except:
        return jsonify({"message": "Camera object passed in value is None"}), status.HTTP_404_NOT_FOUND
    camera_to_add = Camera(camera_name=camera_name, rtsp_url=rtsp_url)
    # check the uniqueness of camera name and its rtsp url
    camera_name_count = Camera.query.filter_by(camera_name=camera_name).count()
    camera_url_count = Camera.query.filter_by(rtsp_url=rtsp_url).count()
    if camera_name_count == 0 and camera_url_count == 0:
        add_to_database(camera_to_add)
        return jsonify({"message": "camera added successfully"}), status.HTTP_200_OK
    else: 
        return jsonify({"message": "fail to add camera"}), status.HTTP_500_INTERNAL_SERVER_ERROR

# function that returns the information of the camera object based on input id 
def query_camera_service(id):
    from models import Camera
    # this replace get_or_404() method
    try: 
        query_item = Camera.query.get(id)
    except:
        return jsonify({"message": "queried camera not existed"}), status.HTTP_404_NOT_FOUND
    converted_item = {}
    for field in [c.key for c in inspect(query_item).mapper.column_attrs]:
        data = query_item.__getattribute__(field)     
        converted_item[field] = data
    return converted_item
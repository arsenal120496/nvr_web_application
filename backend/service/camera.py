from flask import jsonify, Response, json

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
    camera_list = Camera.retrieveList()
    return camera_list

# function that add the input camera object to database
def add_camera_service(user_id, camera_name, rtsp_url):
    from models import Camera
    # check in case camera object passed in from front end is an empty object (NoneType)
    try:
        camera_to_add = Camera(user_id=user_id, camera_name=camera_name, rtsp_url=rtsp_url)
        # check the uniqueness of camera name and its rtsp url
        camera_name_count = Camera.query.filter_by(camera_name=camera_name).count()
        camera_url_count = Camera.query.filter_by(rtsp_url=rtsp_url).count()
        # chỗ này if với else để check nó không bị trùng trong database nên phải return 2 cái trong 
        # block try được ko a, hay bắt buộc chỉ có 1 return statement trong block try
        if camera_name_count == 0 and camera_url_count == 0:
            add_to_database(camera_to_add)
            return Response(json.dumps({"message": "camera added successfully"}), status=200, mimetype='application/json')
        else: 
            return Response(json.dumps({"message": "fail to add camera"}), status=500, mimetype='application/json')

    except Exception as err:
        return Response(json.dumps({"message": "error {}".format(err)}), status=404, mimetype='application/json')
    

# function that returns the information of the camera object based on input id 
def query_camera_service(id):
    from models import Camera
    try: 
        query_camera = Camera.retrieveCamera(id)
        return query_camera
    except:
        return Response(json.dumps({"message": "queried camera not existed"}), status=404, mimetype='application/json')

    
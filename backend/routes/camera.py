from flask import Blueprint, request
from service.camera import *
camera_page = Blueprint('camera_page', __name__)
import json

# all of Flask routes that use Camera services go in here
@camera_page.route('/')
def home():
    return "This is default Camera Page"

# Data format we need from UI: json
# json format: {camera_name: "example", rtsp_url: "www.example.com"}
# tested with postman (succesfully added json data to database)
@camera_page.route('/addCamera', methods=["POST"])
def add_camera():
    camera_object = request.json
    camera_name = camera_object['camera_name']
    rtsp_url = camera_object['rtsp_url']
    user_id = camera_object['user_id']
    if (camera_name is not None) and (rtsp_url is not None) and (user_id is not None):
        add_camera_status = add_camera_service(user_id, camera_name, rtsp_url)
    else:
        return Response(json.dumps({"message": "camera object is NoneType"}), status=404, mimetype='application/json')
    return add_camera_status

# return json data format of camera information depending on id to UI
@camera_page.route('/query/<id>', methods=["GET"])
def query_camera(id):  
    query_result = query_camera_service(id)
    json_result = json.dumps(query_result)
    return json_result
    
# return json data format of list of all cameras information 
@camera_page.route('/getList', methods=["GET"])
def get_list():
    database_list = get_database()
    database_json = json.dumps(database_list)
    return database_json

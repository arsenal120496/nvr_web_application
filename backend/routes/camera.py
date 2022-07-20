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
    return add_camera_service(request.json)

# return json data format of camera information depending on id to UI
@camera_page.route('/query/<id>', methods=["GET"])
def query_camera(id):  
    return json.dumps(query_camera_service(id))
    
# return json data format of list of all cameras information 
@camera_page.route('/getList', methods=["GET"])
def get_list():
    return json.dumps(get_database())

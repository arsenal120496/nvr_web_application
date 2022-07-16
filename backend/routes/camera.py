from flask import Blueprint
from service.camera import *

camera_page = Blueprint('camera_page', __name__)

# all of Flask routes that use Camera services go in here
@camera_page.route('/')
def home():
    return "This is default Camera Page"

@camera_page.route('/addCamera', methods=["POST", "GET"])
def add_camera():
    add_camera_service()
    return "camera added successfully"

@camera_page.route('/query/<id>')
def query_camera(id):
    item = query_camera_service(id)
    return item
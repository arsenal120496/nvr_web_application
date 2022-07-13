from flask import Blueprint
from service.camera import *

camera_page = Blueprint('camera_page', __name__)

# all of Flask routes that use Camera services go in here
@camera_page.route('/')
def home():
    return "This is default Camera Page"


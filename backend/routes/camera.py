from venv import create
from flask import Blueprint
from service.camera import *

camera_page = Blueprint('camera_page', __name__)

# all of Flask routes go in here
@camera_page.route('/')
def home():
    return "day là camera"

@camera_page.route('/delete')
def delete():
    return 'day la delete camera'
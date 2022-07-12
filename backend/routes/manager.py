from flask import Blueprint
from service.manager import *

manager_page = Blueprint('manager_page', __name__)

# all of Flask routes go in here
@manager_page.route('/')
def home():
    return "day là manager"
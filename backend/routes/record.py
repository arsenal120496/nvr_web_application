from flask import Blueprint
from service.record import *

record_page = Blueprint('record_page', __name__)

# all of Record routes that use Camera services go in here
@record_page.route('/')
def home():
    return "This is default record page"
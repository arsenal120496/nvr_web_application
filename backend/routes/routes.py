from flask import Blueprint
from routes.report_members import testing
simple_page = Blueprint('simple_page', __name__)

# all of Flask routes go in here
@simple_page.route('/')
def home():
    testing()
    return "day là home"

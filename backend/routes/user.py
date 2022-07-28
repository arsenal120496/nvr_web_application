from flask import Blueprint, request, Response
from service.user import *
import json

user_page = Blueprint('user_page', __name__)

# all of Flask routes that use User services go in here
@user_page.route("/")
def home():
    return "This is default User Page"

# Data format we need from UI: json
# json format: {username: "abc", password_hash:"123" (encrypted), email:"abc@gmail.com"}
# tested with postman (succesfully added json data to database) (for registration)
@user_page.route("/addUser", methods=["POST"])
def add_user():
    try: 
        user_object = request.json
        username = user_object['username']
        password = user_object['password']
        email = user_object['email']
        # check if the json data passed in from UI is not None 
        if (username is not None) and (password is not None) and (email is not None):
            add_user_status = add_user_service(username, password, email)
            # check if the User object already exist in the database
            if add_user_status == {}:
                return Response(json.dumps({"message": "fail to add user account, already exist in the database"}), status=412, mimetype='application/json')
            else:
                return Response(json.dumps(add_user_status), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({"message": "User object is NoneType"}), status=404, mimetype='application/json')
    except Exception as err:
        return Response(json.dumps({"message": "fail to add User account, error {}".format(err)}), status=404, mimetype='application/json')

# return json data format of user account information depending on id to UI
@user_page.route('/query/<id>', methods=["GET"])
def query_user(id):  
    try:   
        query_result = query_user_service(id)
        if (query_result is None or query_result == {}):
            return Response(json.dumps({"message": "no User object at given id"}),status=203, mimetype='application/json')
        else: 
            return Response(json.dumps(query_result), status=200, mimetype='application/json')
    except Exception as err:
        return Response(json.dumps({"message": "error {}".format(err)}), status=404, mimetype='application/json')
    
# return json data format of list of all user account information 
@user_page.route('/getList', methods=["GET"])
def get_list():
    try:
        database_list = get_database()
        database_json = json.dumps(database_list)
        return Response(database_json, status=200, mimetype='application/json')
    except Exception as err:
        return Response(json.dumps({"message": "error {}".format(err)}), status=404, mimetype="application/json")


@user_page.route('/authenticator', methods=["POST"])
def authenticator():
    try: 
        user_object = request.json
        username = user_object['username']
        password = user_object['password']
        email = user_object['email']
        # check if the json data passed in from UI is not None 
        if (username is not None) and (password is not None) and (email is not None):
            if(verify_service(username, password, email)[0]):
                verify_service_status = verify_service(username, password, email)[1]
                return Response(json.dumps(verify_service_status), status=200, mimetype='application/json')
            # check if the User object already exist in the database
            else:
                verify_service_status = verify_service(username, password, email)[1]
                return Response(json.dumps(verify_service_status), status=404, mimetype='application/json')
        else:
            return Response(json.dumps({"message": "User object is NoneType"}), status=404, mimetype='application/json')
    except Exception as err:
        return Response(json.dumps({"message": "fail to check User account's credentials, error {}".format(err)}), status=404, mimetype='application/json')




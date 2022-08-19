from flask import Blueprint, request, Response
from service.camera import CameraService
import json

camera_page = Blueprint('camera_page', __name__)

# all of Flask routes that use Camera services go in here
@camera_page.route('/')
def home():
    return "This is default Camera Page"

# Data format we need from UI: json
# json format: {camera_name: "example", rtsp_url: "www.example.com", user_id: 1}
# tested with postman (succesfully added json data to database)
@camera_page.route('/addCamera', methods=["POST"])
def add_camera():
    try: 
        camera_object = request.json
        camera_name = camera_object['camera_name']
        rtsp_url = camera_object['rtsp_url']
        user_id = camera_object['user_id']
        # check if the json data passed in from UI is not None 
        if (camera_name is not None) and (rtsp_url is not None) and (user_id is not None):
            add_camera_status = CameraService.add_camera_service(user_id, camera_name, rtsp_url)
            # check if the Camera object already exist in the database
            if add_camera_status == {}:
                return Response(json.dumps({"message": "fail to add camera, already exist in the database"}), status=412, mimetype='application/json') 
            else:
                return Response(json.dumps(add_camera_status), status=200, mimetype='application/json')
        else:
            return Response(json.dumps({"message": "camera object is NoneType"}), status=404, mimetype='application/json')
    except Exception as err:
        return Response(json.dumps({"message": "fail to add camera, error {}".format(err)}), status=404, mimetype='application/json')

# return json data format of camera information depending on id to UI
@camera_page.route('/query/<id>', methods=["GET"])
def query_camera(id):
    try:   
        query_result = CameraService.query_camera_service(id)
        if (query_result is None or query_result == {}):
            return Response(json.dumps({"message": "no camera object at given id"}),status=203, mimetype='application/json')
        else: 
            return Response(json.dumps(query_result), status=200, mimetype='application/json')
    except Exception as err:
        return Response(json.dumps({"message": "error {}".format(err)}), status=404, mimetype='application/json')
        
# return json data format of list of all cameras information 
@camera_page.route('/getList', methods=["GET"])
def get_list():
    try:
        database_list = CameraService.get_database()
        database_json = json.dumps(database_list)
        return Response(database_json, status=200, mimetype='application/json')
    except Exception as err:
        return Response(json.dumps({"message": "error {}".format(err)}), status=404, mimetype="application/json")

@camera_page.route('/rtmp', methods=["GET"])
def generate_rtmp():
    try: 
        import subprocess as sp
        command = ['ffmpeg', '-hide_banner', '-loglevel', 
        'warning', '-avoid_negative_ts', 'make_zero', '-fflags',
         '+genpts+discardcorrupt', '-rtsp_transport', 'tcp', '-stimeout',
          '5000000', '-use_wallclock_as_timestamps', '1', '-i', 
          'rtsp://tic-viewer:20202021%40Tm%40@192.168.85.107/Streaming/Channels/101/?transportmode=unicast',
           '-c', 'copy', '-f', 'flv', 'rtmp://localhost/live/back1', '-r', '5', '-s', 
           '1280x720', '-f', 'rawvideo', '-pix_fmt', 'rgb24', 'pipe:']
        pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
        return Response(CameraService.retrieve_rtmp(pipe), status=200, mimetype="multipart/x-mixed-replace; boundary=frame")
    except Exception as err:
        return Response(json.dumps({"message": "error {}".format(err)}), status=404, mimetype='application/json')
    

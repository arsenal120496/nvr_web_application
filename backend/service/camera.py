# function that adds the input object to the database
from asyncio.subprocess import STDOUT
from tracemalloc import start
import cv2

def add_to_database(object):
    try: 
        from app import db
        db.session.add(object)
        db.session.commit()
    except Exception as err:
        return {"message": "fail to add camera object, err {}".format(err)}

# function that deletes the input object to the database
def delete_from_database(object):
    try:
        from app import db 
        from models import Camera
        item_id = object.camera_id
        delete_item = Camera.query.get(item_id)
        db.session.delete(delete_item)
        db.session.commit()
    except Exception as err:
        return {"message": "fail to delete camera object, err {}".format(err)}
    
# function that change the input object's camera name to target name
def change_camera_name(object, target_name):
    try: 
        from app import db
        from models import Camera
        item_id = object.camera_id
        update_item = Camera.query.get(item_id)
        update_item.camera_name = target_name
        db.session.commit()
    except Exception as err:
        return {"message": "fail to update camera object, err {}".format(err)}

# function that change the input object's camera url to target url
def change_camera_url(object, target_url):
    try: 
        from app import db
        from models import Camera
        item_id = object.camera_id
        update_url = Camera.query.get(item_id)
        update_url.rtsp_url = target_url
        db.session.commit()
    except Exception as err:
        return {"message": "fail to update camera's rtsp url, err {}".format(err)}

# function that return the list of all camera objects currently in the database
def get_database():
    try:
        from models import Camera
        camera_list = Camera.retrieveList()
        return camera_list
    except Exception as err:
        return {"message": "fail to retrieve camera list from database, err {}".format(err)}

# function that add the input camera object to database
def add_camera_service(user_id, camera_name, rtsp_url):
    from models import Camera
    # check in case camera object passed in from front end is an empty object (NoneType)
    try:
        camera_to_add = Camera(user_id=user_id, camera_name=camera_name, rtsp_url=rtsp_url)
        # check the uniqueness of camera name and its rtsp url
        camera_name_count = Camera.query.filter_by(camera_name=camera_name).count()
        camera_url_count = Camera.query.filter_by(rtsp_url=rtsp_url).count()
        if camera_name_count == 0 and camera_url_count == 0:
            add_to_database(camera_to_add)
            return {"message": "camera added successfully"}
        else: 
            return {}
    except Exception as err:
        return {"message": "error {}".format(err)}
    

# function that returns the information of the camera object based on input id 
def query_camera_service(id):
    from models import Camera
    try: 
        query_camera = Camera.retrieveCamera(id)
        return query_camera
    except Exception as err:
        return {"message": "error {}".format(err)}

def retrieve_rtmp(p):
    count = 0
    # while True:
    #     raw_img = p.stdout
    #     print("raw_img", raw_img)
    #     print(" type raw_img", type(raw_img))
    #     _, jpg = cv2.imencode(".jpg", raw_img, [int(cv2.IMWRITE_JPEG_QUALITY),70])
    #     yield (b'--frame\r\n'
    #            b'Content-Type: image/jpeg\r\n\r\n' + jpg.tobytes() + b'\r\n\r\n')
    # cmd = "ffmpeg -hide_banner -loglevel warning -re -stream_loop -1 -fflags +genpts -i rtsp://tic-viewer:20202021%40Tm%40@192.168.85.107/Streaming/Channels/101/?transportmode=unicast -c copy -f flv rtmp://localhost/live/test -r 5 -s 1280x720 -f rawvideo -pix_fmt yuv420p pipe: "
    for data in iter(p.stdout.readline, ''):
        count+=1
        _, jpg = cv2.imencode(".jpg", data, [int(cv2.IMWRITE_JPEG_QUALITY),70])
        cv2.imwrite("C:\\Users\\vinhh\\Desktop\\nvr_web_application\\backend\\images\\id_{}".format(count), jpg)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg.tobytes() + b'\r\n\r\n')
        # print("data", data)
        

    # while True:
    #     print("đây là out.stdout", out.stdout.readline)
    #     print(type(out.stdout))
    # return out.stdout 
    # while True:

    # for data in iter(p.stdout.readline, b''):

    

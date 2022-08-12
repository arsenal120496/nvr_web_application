from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from init_app import init_db, init_blueprint, set_config, CameraObject
from flask_migrate import Migrate
import threading
import subprocess
import time
import numpy as np

app = Flask(__name__)
# set the configuration for the application
app.config["ENV"] = "development"
set_config(app)
# prevent CORS
CORS(app)

# set up the database and model
db = SQLAlchemy()
migrate = Migrate()
init_db(app)

# set up the blueprint for routes that manipulate the database 
init_blueprint(app)
camera_obj = CameraObject()
cmd = "ffmpeg -hide_banner -loglevel warning -re -stream_loop -1 -fflags +genpts -i rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4 -c copy -f flv rtmp://localhost/live/test -r 5 -s 1280x720 -f rawvideo -pix_fmt yuv420p pipe: "
# cmd = "ffmpeg -hide_banner -loglevel warning -re -stream_loop -1 -fflags +genpts -i rtsp://tic-viewer:20202021%40Tm%40@192.168.85.107/Streaming/Channels/101/?transportmode=unicast -c copy -f flv rtmp://localhost/live/test -r 5 -s 1920x1080 -f rawvideo -pix_fmt yuv420p pipe:"
# cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'warning', '-re', '-stream_loop', '-1', '-fflags', '+genpts', '-i', 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4', '-c', 'copy', '-f', 'flv', 'rtmp://localhost/live/test', '-r', '5', '-s', '1280x720', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', 'pipe:']
# cmd = ["ffmpeg", "-i", "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4", "-c", "copy", "-f", "flv", "rtmp://localhost:1935/live/test", '-r', '5', '-s', '1280x720', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', 'pipe:']
# cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'warning', '-stream_loop', '-1', '-fflags', '+genpts', 'tcp', '-stimeout', '5000000', '-use_wallclock_as_timestamps', '1', '-i', 'rtsp://tic-viewer:20202021%40Tm%40@192.168.85.107/Streaming/Channels/101/?transportmode=unicast', '-c', 'copy', '-f', 'flv', 'rtmp://localhost/live/back1', '-r', '5', '-s', '1280x720', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', 'pipe:']
# cmd = 'ffmpeg -hide_banner -loglevel warning -re -stream_loop -1 -fflags +genpts -i rtsp://tic-viewer:20202021%40Tm%40@192.168.85.107/Streaming/Channels/101/?transportmode=unicast -c copy -f flv rtmp://0.0.0.0/live/test -r 5 -s 1920x1080 -f rawvideo -pix_fmt yuv420p pipe: '
# cmd = ['ffmpeg', '-hide_banner', '-loglevel', 'warning', '-avoid_negative_ts', 'make_zero', '-fflags', '+genpts+discardcorrupt', '-rtsp_transport', 'tcp', '-stimeout', '5000000', '-use_wallclock_as_timestamps', '1', '-i', 'rtsp://tic-viewer:20202021%40Tm%40@192.168.85.107/Streaming/Channels/101/?transportmode=unicast', '-c', 'copy', '-f', 'flv', 'rtmp://localhost/live/back1', '-r', '5', '-s', '1280x720', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', 'pipe:']
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, bufsize=600*600, universal_newlines=True)

def update_frame(b, camera_obj):
    time.sleep(5)
    for line in p.stdout:
        print("line", line)
        frame = np.fromstring(line, dtype=np.uint)
        camera_obj.update_frame(frame)
    # while True:
    #     b = p.stdout
    #     print(b)
    #     frame = np.frombuffer(b)
    #     camera_obj.update_frame(frame)
threading.Thread(target=update_frame, args=(p, camera_obj, )).start()
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)







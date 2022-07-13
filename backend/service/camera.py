# function that adds the input object to the database
def add_to_database(object):
    from app import db
    db.session.add(object)
    db.session.commit()

# function that deletes the input object to the database
def delete_from_database(object):
    from app import db 
    from models import Camera
    item_id = object.camera_id
    delete_item = Camera.query.get_or_404(item_id)
    db.session.delete(delete_item)
    db.session.commit()

# function that change the input object's camera name to target name
def change_camera_name(object, target_name):
    from app import db
    from models import Camera
    item_id = object.camera_id
    update_item = Camera.query.get_or_404(item_id)
    update_item.camera_name = target_name
    db.session.commit()

# function that change the input object's camera url to target url
def change_camera_url(object, target_url):
    from app import db
    from models import Camera
    item_id = object.camera_id
    update_item = Camera.query.get_or_404(item_id)
    update_item.url = target_url
    db.session.commit()

    
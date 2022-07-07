from models.cam_model import Record,db

def testing():
    record = Record(task_name="huy",completed=True)
    db.session.add(record)
    db.session.commit()
    print("testing")
    return "123"
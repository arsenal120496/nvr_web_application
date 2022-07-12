from app import db

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(240))
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, task_name, completed):
        self.task_name = task_name
        self.completed = completed
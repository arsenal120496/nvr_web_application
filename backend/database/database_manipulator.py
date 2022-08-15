class Database():
    def save():
        from app import db 
        db.session.commit()
    def add(object):
        from app import db
        db.session.add(object)
        db.session.commit()
    def delete(object):
        from app import db
        db.session.delete(object)
        db.session.commit()
        
    
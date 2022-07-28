from app import db 
from sqlalchemy.inspection import inspect
from passlib.hash import sha256_crypt
from configs.config import Config


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(240), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(240), nullable=False, unique=True)

    @property 
    def password(self):
        raise AttributeError("password is not a readable attribute")
    
    @password.setter 
    def password(self, password):
        self.password_hash = sha256_crypt.encrypt(password + Config.SECRET_KEY)

    def verify_password(self,password):
        return sha256_crypt.verify(password + Config.SECRET_KEY, self.password_hash)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def retrieveList():
        try: 
            all_users = User.query.all()
            user_list = []
            for i in range(len(all_users)):
                user_dictionary = all_users[i].toDict()
                user_list.append(user_dictionary)
            return user_list
        except Exception as err:
            return {"message": "error {}".format(err)}

    def retrieveUser(id):
        try: 
            query_item = User.query.get(id)
            query_dictionary = User.toDict(query_item)
            return query_dictionary
        except Exception as err:
            return {"message": "error {}".format(err)}    

    def update(id, updating_item):
        try:
            object = User.query.get(id)
            object.username = updating_item['username']
            object.password = updating_item['password_hash']
            object.email = updating_item['email']
            db.session.commit()
            return {"message": "item updated successfully"}
        except Exception as err:    
            return {"message": "error {}".format(err)}

    def delete(id):
        try: 
            delete_item = User.query.filter_by(camera_id=id).first()
            db.session.delete(delete_item)
            db.session.commit()
            return {"message": "user account deleted successfully"}
        except Exception as err:
            return {"message": "error {}".format(err)}
    
    def toDict(user_object):
        try:
            converted_item = {}
            if user_object is None:
                return {}
            else:
                for field in [c.key for c in inspect(user_object).mapper.column_attrs]:
                    data = user_object.__getattribute__(field)     
                    converted_item[field] = data
                return converted_item
        except Exception as err: 
            return {"message": "error {}".format(err)}
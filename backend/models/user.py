from app import db 
from sqlalchemy.inspection import inspect
from passlib.hash import sha256_crypt
from configs.config import Config
import logging 
from database.database_manipulator import Database


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
            logging.info("User list retrieved successfully")
            return user_list
        except Exception as err:
            logging.warning("Fail to retrieve user list, err {}".format(err))
            return {"message": "error {}".format(err)}

    def retrieveUser(id):
        try: 
            query_item = User.query.get(id)
            query_dictionary = User.toDict(query_item)
            logging.info("User account retrieved successfully")
            return query_dictionary
        except Exception as err:
            logging.warning("Fail to retrieve user account, err {}".format(err))
            return {"message": "error {}".format(err)}    

    def update(id, updating_item):
        try:
            object = User.query.get(id)
            object.username = updating_item['username']
            object.password = updating_item['password_hash']
            object.email = updating_item['email']
            Database.save()
            logging.info("User account updated successfully")
            return {"message": "User account updated successfully"}
        except Exception as err:   
            logging.warning("Fail to update user account, err {}".format(err)) 
            return {"message": "error {}".format(err)}

    def delete(id):
        try: 
            delete_item = User.query.filter_by(camera_id=id).first()
            Database.delete(delete_item)
            logging.info("User account deleted successfully")
            return {"message": "user account deleted successfully"}
        except Exception as err:
            logging.warning("Fail to delete user account, err {}".format(err))
            return {"message": "error {}".format(err)}
    
    def toDict(user_object):
        try:
            converted_item = {}
            if user_object is None:
                logging.info("User account object is NoneType")
                return {}
            else:
                for field in [c.key for c in inspect(user_object).mapper.column_attrs]:
                    data = user_object.__getattribute__(field)     
                    converted_item[field] = data
                logging.info("Successfully convert user account object to dictionary")
                return converted_item
        except Exception as err: 
            logging.warning("Fail to convert user account object to dictionary, err {}".format(err))
            return {"message": "error {}".format(err)}
from sqlalchemy.inspection import inspect
# function that adds the input object to the database
def add_to_database(object):
    try: 
        from app import db
        db.session.add(object)
        db.session.commit()
    except Exception as err:
        return {"message": "fail to add User object, err {}".format(err)}

# function that deletes the input object to the database
def delete_from_database(object):
    try:
        from app import db 
        from models import User
        item_id = object.user_id
        delete_item = User.query.get(item_id)
        db.session.delete(delete_item)
        db.session.commit()
    except Exception as err:
        return {"message": "fail to delete User object, err {}".format(err)}

# function that return the list of all user objects currently in the database
def get_database():
    try:
        from models import User
        user_list = User.retrieveList()
        return user_list
    except Exception as err:
        return {"message": "fail to retrieve user list from database, err {}".format(err)}

# function that add the input user object to database (for registration)
def add_user_service(username, password, email):
    from models import User
    # check in case user object passed in from front end is an empty object (NoneType)
    try:
        user_to_add = User(username, password, email)
        # check to see if the user's information is unique in the database
        # only username and email are checked unique, password could be similar to other users
        username_count = User.query.filter_by(username=username).count()
        email_count = User.query.filter_by(email=email).count()
        # in case there is no such account in the database yet
        if username_count == 0 and email_count == 0:
            add_to_database(user_to_add)
            return {"message": "user account added successfully"}
        # in case there has already been an account in the database
        else: 
            return {}
    except Exception as err:
        return {"message": "error {}".format(err)}
   

# function that returns the information of the user object based on input id 
def query_user_service(id):
    from models import User
    try: 
        query_user = User.retrieveUser(id)
        return query_user
    except Exception as err:
        return {"message": "error {}".format(err)}
    
# function that check whether the input requirements are valid
def verify_service(username, password, email):
    from models import User
    try: 
        # query based on username and email
        item = User.query.filter_by(username=username,email=email).first()
        # if account exist based on username and email, validate its password
        if (item is not None):
            if(item.verify_password(password)):
                # return message indicate account has been verified if the password is validated
                return (True, {"message": "account verified successfully"})
            else:
                return (False, {"message": "incorrect password"})
        else:
            return (False, {"message": "username or email not existed"})
    except Exception as err:
        return {"message": "error {}".format(err)}






        

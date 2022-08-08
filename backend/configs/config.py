class Config(object):
    # all of the classes below is going to inherit these variables
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY='\xd9\x11\xe3\xc8\xfct\x1c\xd6\xbe\xdc\xdc|X\xaf\xd4\x1a\x94\xbcy\xb4ki\x82\xda'
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    # interactive debugger will be shown for unhandled exceptions
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CORS_HEADERS = 'Content-Type'
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/testing_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CORS_HEADERS = 'Content-Type'
    SESSION_COOKIE_SECURE = False



import os


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY", "testingSecretKey335342")
    DEBUG = False
    TESTING = False
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    SERVER_NAME = os.environ.get('SERVER_NAME')
    PORT = os.environ.get("PORT")
    




class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False



config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
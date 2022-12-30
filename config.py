import os


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY", "testingSecretKey335342")
    DEBUG = False
    TESTING = False
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    ALLOWED_HOST = ['*']
    HOST = "imageapi-production-2dd9.up.railway.app"
    port =  os.getenv("PORT", default=5000)




class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False



config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
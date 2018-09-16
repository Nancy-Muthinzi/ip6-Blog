import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-student:ms@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    @staticmethod
    def init_app(app):
        pass
        
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig,
# 'test':TestConfig
}        

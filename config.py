import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'advasgdv6r234b34837834864'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    KUTI_MAIL_SUBJECT_PREFIX = '[KUTI]'
    KUTI_MAIL_SENDER = 'KUTI admin <kuti@sweskills.com>'
    KUTI_ADMIN_USERNAME = os.environ.get('KUTI_ADMIN_USERNAME')
    KUTI_ADMIN_PASSWORD = os.environ.get('KUTI_ADMIN_PASSWORD')
    KUTI_POST_PER_PAGE = 10
    KUTI_FOLLOWERS_PER_PAGE = 10
    KUTI_FOLLOWED_PER_PAGE = 10
    KUTI_COMMENTS_PER_PAGE = 10
    LIVE_URL = "http://kuti.ml"


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or\
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI =\
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:////' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

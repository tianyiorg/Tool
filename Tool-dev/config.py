
import logging


class Config(object):
    DEBUG = True
    SECRET_KEY = "PM2T2qaNEVQA/QFsojPW+PkJjb9JFvc+6lXrD9iZcZfTyiamJQM/0gQ1vWbFKlZxh9bRCS352NGj2spG9TpDXg=="
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/tools"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    '''开发环境的配置'''
    DEBUG = True


class ProductionConfig(Config):
    '''生产环境的配置'''
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    '''单元测试环境的配置'''
    DEBUG = True
    Testing = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig}


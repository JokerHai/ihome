# -*- coding: utf-8 -*-
# 项目配置文件
# @Author  : joker
# @Date    : 2018-12-27 test
import logging
from  redis import StrictRedis

class Config:
    # 密钥
    SECRET_KEY = "QWE123!@#"

    # MYSQL配置

    # sqlHost地址
    MYSQL_DB_HOST = 'localhost'

    # sql用户名
    MYSQL_DB_USERNAME = 'root'

    # sql密码
    MYSQL_DB_PASSWORD = 'root'

    # sql端口
    MYSQL_DB_PORT = "3306"

    # dbName
    MYSQL_DB_NAME = 'db_home'

    # 该字段增加了大量的开销,会被禁用,建议设置为False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    #redis配置
    REDIS_HOST = 'localhost'

    REDIS_PORT = "6379"

    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中

    # 让 cookie 中的 session_id 被加密签名处理
    SESSION_USE_SIGNER = True

    # 使用 redis 的实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    # session 的有效期，单位是秒
    PERMANENT_SESSION_LIFETIME = 86400


    #默认日志等级
    LOG_LEVEL = logging.DEBUG

    @staticmethod
    def init_app(app):
        pass
    
#开发环境配置文件
class DevelopmentConfig(Config):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql://"+\
        Config.MYSQL_DB_USERNAME+":"+Config.MYSQL_DB_PASSWORD+"@"+Config.MYSQL_DB_HOST+":"+Config.MYSQL_DB_PORT+"/"+Config.MYSQL_DB_NAME

class ProductionConfig(Config):

    #生产模式下的配置
    LOG_LEVEL = logging.ERROR

    @classmethod
    def init_app(cls,app):

        Config.init_app(app)

config = {
    'development' : DevelopmentConfig,
    'production'  : ProductionConfig,
    'default'     : DevelopmentConfig
}
# -*- coding: utf-8 -*-
# 日志配置
# @Author  : joker
# @Date    : 2018-12-29
import datetime
import logging
from logging.handlers import RotatingFileHandler

def setup_log(level_name):
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=level_name)  # 调试debug级

    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/"+datetime.datetime.now().strftime('%Y-%m-%d')+".log", maxBytes=1024 * 1024 * 100, backupCount=10)

    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')

    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)

    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)




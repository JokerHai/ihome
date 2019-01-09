# -*- coding: utf-8 -*-
#开启蓝图
# @Author  : joker
# @Date    : 2018-12-27

from  flask import  Blueprint

main = Blueprint('main',__name__)

from ..main import views, errors

from  ..common import constants



@main.app_context_processor
def inject_permissions():
    return dict(constants = constants)
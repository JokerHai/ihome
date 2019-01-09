# -*- coding: utf-8 -*-
#首页入口文件
# @Author  : joker
# @Date    : 2018-12-27
from  flask import render_template
from flask_login import current_user

from ..main import main

@main.route('/',methods = ['GET'])
def index():
    print(current_user.is_authenticated)
    return  render_template("site/index.html")

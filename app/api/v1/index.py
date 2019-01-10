# -*- coding: utf-8 -*-
#首页轮播图
# @Author  : joker
# @Date    : 2019-01-10
from app.common.response_code import RET
from ..v1 import api
from flask import jsonify


@api.route('/houses_index',methods = ['GET'])
def houses_index():

    return jsonify(status=RET.OK, errmsg="OK")
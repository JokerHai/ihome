from functools import wraps

from flask import current_app
from flask import g
from flask import render_template, jsonify
from flask import request
from flask import session
from app.common.response_code import RET
from app.models import House, User
from . import api


@api.route('/v1/myhouse',methods = ['GET'])
def myhouse():

    user = g.user
    # 1. 取出当前用户real_name,id_card 判断是否认证
    try:
        real_name = User.query.filter(User.real_name).first()
        id_card = User.query.filter(User.id_card).first()

        if not all([real_name, id_card]):
            return ""
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="该用户未认证")

    # 2.获取房屋
    houses=[]
    try:
        houses = House.query.order_by(House.create_time()).all()
    except Exception as e:
        current_app.logger.error(e)

    # 3.将房屋对象列表,转成字典列表
    houses_list = []
    for house in houses:
        houses_list.append(house.to_basic_dict())

    #4.返回响应
    return render_template('house/myhouse.html',houses_list=houses_list)

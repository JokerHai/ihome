from functools import wraps

from flask import current_app
from flask import g
from flask import render_template, jsonify
from flask import request
from flask import session
from app.common.response_code import RET
from app.models import House, User
from . import api


@api.route('/myhouse',methods = ['GET'])
def myhouse():

    # 获取用户的登陆信息
    user_id = session.get("user_id")

    # 通过user_id取出用户对象
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)
    if not user:
        return jsonify(errno=RET.DBERR,errmsg="")

    # 1. 取出当前用户real_name,id_card 判断是否认证
    if not all([user.real_name, user.id_card]):
        return render_template('house/myhouse.html',real_name=None,id_card=None)

    # # 2.获取房屋
    houses=[]
    try:
        houses = House.query.filter(House.user_id == user.id).order_by(House.create_time.desc()).all()
    except Exception as e:
        current_app.logger.error(e)

    # 3.将房屋对象列表,转成字典列表
    houses_list = []
    for house in houses:
        houses_list.append(house.to_basic_dict())
    
    #4.返回响应
    return render_template('house/myhouse.html',houses_list=houses_list,real_name=user.real_name,id_card=user.id_card)

from functools import wraps

from flask import current_app
from flask import g
from flask import redirect
from flask import render_template, jsonify
from flask import request
from flask import session

from app import db
from app.common.image_storage import image_storage
from app.common.response_code import RET
from app.models import House
from . import api

#定义登陆装饰器,封装用户的登陆数据
# def user_login_data(view_func):
#     @wraps(view_func)
#     def wrapper(*args,**kwargs):
#         # 1.从session中取出用户的user_id
#         user_id = session.get("user_id")
#
#         # 2通过user_id取出用户对象
#         user = None
#         if user_id:
#             try:
#                 from app.models import User
#                 user = User.query.get(user_id)
#             except Exception as e:
#                 current_app.logger.error(e)
#
#         #3.将user数据封装到g对象
#         g.user = user
#
#         return view_func(*args,**kwargs)
#     return wrapper



@api.route("/v1/newhouse", methods=["GET"])
# @user_login_data
def house_index():

    # if not g.user:
    #     return redirect("/")
    #
    # # 1.获取参数
    # user_id = g.user_id
    # title = request.json.get("title")
    # price = request.json.get("price")
    # area_id = request.json.get("area_id")
    # address = request.json.get("address")
    # room_count = request.json.get("room_count")
    # acreage = request.json.get("acreage")
    # unit = request.json.get("unit")
    # capacity = request.json.get("capacity")
    # beds = request.json.get("beds")
    # deposit = request.json.get("deposit")
    # min_days = request.json.get("min_days")
    # max_days = request.json.get("max_days")
    # facility = request.json.get("facility")
    #
    # # 2. 校验参数,为空校验
    # if not all([title,price,area_id, address,room_count,acreage,unit,capacity,beds,deposit,min_days,max_days,facility]):
    #     return jsonify(errno=RET.PARAMERR, errmsg="参数不全")
    #
    # # 3. 创建房源对象,设置属性
    # house = House()
    # house.user_id = user_id
    # house.title = title
    # house.price = price
    # house.area_id = area_id
    # house.address = address
    # house.room_count = room_count
    # house.acreage = acreage
    # house.unit = unit
    # house.capacity = capacity
    # house.beds = beds
    # house.deposit = deposit
    # house.min_days = min_days
    # house.max_days = max_days
    #
    # # 4. 保存到数据
    # try:
    #     db.session.add(house)
    #     db.session.commit()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DBERR, errmsg="房源发布失败")

    # 5. 返回响应
    # return jsonify(errno=RET.OK, errmsg="发布成功")

    # return  render_template('newhouse/../../static/html/newhouse.html')

    return current_app.send_static_file("html/" + "newhouse.html")
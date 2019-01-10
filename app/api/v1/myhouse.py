from functools import wraps

from flask import current_app
from flask import g
from flask import render_template, jsonify
from flask import session

from app.common.response_code import RET
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


# 我的列表
# 请求路径: /api/v1/newhouse
# 请求方式:GET7
# 请求参数:p，id_card
# 返回值:GET渲染myhouse.html页面

@api.route('/v1/myhouse',methods = ['GET'])
def myhouse():
    return current_app.send_static_file("html/"+"myhouse.html")
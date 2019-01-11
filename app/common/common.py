# -*- coding: utf-8 -*-
# 公共方法
# @Author  : joker
# @Date    : 2019-01-02
from functools import wraps
from flask import session, current_app, g
import re


# 效验手机号
from flask import current_app
from flask import g
from flask import session
from functools import wraps


def check_mobile(mobile):
    if mobile is not None:
        if re.match("1[3-9]\d{9}", mobile) is not None:
            return True
        else:
            return False
    else:
        return False
#定义登陆装饰器,封装用户的登陆数据
def user_login_data(view_func):
    @wraps(view_func)
    def wrapper(*args,**kwargs):
        # 1.从session中取出用户的user_id
        user_id = session.get("user_id")

        # 2通过user_id取出用户对象
        user = None
        if user_id:
            try:
                from app.models import User
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)

        #3.将user数据封装到g对象
        g.user = user

        return view_func(*args,**kwargs)
    return wrapper

# 定义登录装饰器，封装用户的登录数据
def user_login_data(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        # 1.从session中取出用户的user_id
        user_id = session.get("user_id")
        user = None
        if user_id:
            # 2.通过user_id取出用户对象
            try:
                from app.models import User
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)
        # 3.将user数据封装到g对象
        g.user = user
        return view_func(*args, **kwargs)
    return wrapper



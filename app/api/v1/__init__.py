# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-28

from flask import Blueprint

api = Blueprint('api',__name__)


from ..v1 import views, area,myhouse,newhouse, users,profile, booking, index,house_info,order_zhuyi, search,order

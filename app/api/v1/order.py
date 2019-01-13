# -*- coding: utf-8 -*-
#订单下单
# @Author  : joker
# @Date    : 2019-01-13
from flask import request
from flask_login import login_required

from ..v1 import api

# @login_required
# @api.route('/house_testing',methods = ['GET','POST'])
# def house_testing():
#
#     # ids = request.args.get('ids')
#     #
#     # return  ids
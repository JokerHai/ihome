# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-28
from flask import abort
from flask import current_app, jsonify
from flask import g
from flask import render_template
from flask import request

from app.common.response_code import RET
from app.models import House
from ..v1 import api


# 请求路径:/api/v1/houses
# 请求方式:GET
# 请求参数:p
# 返回值:total_page,houses
@api.route('/house_list')
def house_list():
    # 获取参数,为空校验
    page = request.args.get('p',1)
    # 类型转换
    try:
        page = int(page)
    except Exception as e:
        page = 1
    # 分页查询可入住的房源,总页数,当前页,和当前页对象
    filter_list =[]
    try:
        paginates = House.query.order_by(House.ctime.desc()).paginate(page,5,False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='获取房屋信息失败')
    # 取出相关信息,
    totalpage = paginates.pages
    currentpage=paginates.page
    items = paginates.items
    # 将当前页对象列表转换成字典列表
    houses_list =[]
    for house in items:
        houses_list.append(house.to_full_dict())
    # 携带数据,渲染页面
    data= {
        'totalpage':totalpage,
        'currentpage':currentpage,
        'houses_list':houses_list
    }
    return render_template('house_info_list/search.html',data=data)

# 请求路径:/api/v1/houses/\<int:house_id>
# 请求方式:GET
# 请求参数:house_id
# 返回值:user_id,house
@api.route('/houses/<int:house_id>')
def houses(house_id):
    # 根据房屋id查询出房源对象,
    try:
        house = House.query.get(house_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='获取房屋信息失败')
    #不存在直接抛出异常
    if not house:
        abort(404)

    # 判断用户是否登陆,且为房东,
    is_like = False
    if g.user and (g.user.id == house.user_id):
       is_licke = True
    data = {
        'house':house.to_full_dict(),
        'is_like':is_like
    }
    return render_template('house_info_list/detail.html',data=data)

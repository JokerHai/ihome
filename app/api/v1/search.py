# -*- coding: utf-8 -*-
#列表页相关
# @Author  : joker
# @Date    : 2019-01-11
from flask import render_template, jsonify, request, current_app
from flask_login import current_user

from app.common.response_code import RET
from ...common import constants
from app.models import House
from ..v1 import api


@api.route('/search_view',methods = ['GET'])
def search_view():
    return render_template('search/search.html')

@api.route('/houses_list',methods = ['GET'])
def houses_list():
    try:
        # 分页
        page = request.args.get('page', 1, type=int)

        # 区域Id
        aid = request.args.get('aid')

        # 开始日期
        sd = request.args.get('sd')

        # 结束日期
        ed = request.args.get('ed')

        # 排序
        sk = request.args.get('sk')

        filters = []

        if aid :
            filters.append(House.area_id == aid)
        if sd :
            filters.append(House.create_time >= sd)
        if ed :
            filters.append(House.create_time <= ed)

        if sk == "booking":
            order = House.order_count.desc()
        elif sk == "price-inc":
            order = House.price.asc()
        elif sk == "price­ des":
            order = House.price.desc()
        else:
            order = House.create_time.desc()
        pagination = House.query.filter(*filters).order_by(order).paginate(
            page,per_page = constants.HOME_POSTS_PER_PAGE,
            error_out= False
        )
        houses = pagination.items
        return jsonify(
                status = RET.OK,
                errmsg = "请求成功",
                data   = {
                    'houses':[house.to_basic_dict() for house in houses]
                },
                total_page = pagination.total
        )
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=RET.DBERR, errmsg="程序异常，请联系管理员")

@api.route('/show_detail/<int:ids>',methods = ['GET'])
def show_detail(ids):
    houses = House.query.get_or_404(ids)

    data = {'house':houses.to_full_dict()}

    return render_template('search/detail.html',data = data)
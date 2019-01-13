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

@api.route('/show_detail/<int:id>',methods = ['GET'])
def show_detail(id):
    print(current_user.id)
    data = {
        "house":{
            "acreage": 5,
            "address": "我是地址",
            "beds": "5张床",
            "capacity": 5,
            "comments":[{
                "comment": "哎哟不错哟",
                "ctime": "2017-11-14 11:17:07",
                "user_name": "匿名用户"
            }],
            "deposit": 500,
            "facilities":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
            "hid": 4,
            "img_urls": [
                "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=285959312,3266930479&fm=27&gp=0.jpg",
                "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3636400456,4056026476&fm=27&gp=0.jpg"
            ],
            "max_days": 5,
            "min_days": 5,
            "price": 500,
            "room_count": 5,
            "title": "555",
            "unit": "5",
            "user_avatar": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2879950569,4061525608&fm=27&gp=0.jpg",
            "user_id": 1,
            "user_name": "哈哈哈哈哈哈"
        },
        "user_id": 1
    }
    return render_template('search/detail.html',data = data)
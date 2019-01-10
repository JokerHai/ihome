# -*- coding: utf-8 -*-
# 获取地区相关
# @Author  : joker
# @Date    : 2019-01-10
from flask import current_app
from flask import jsonify

from app.common.response_code import RET
from app.models import Area
from ..v1 import api


@api.route('/get_area_list', methods=['GET'])
def get_area_list():
    try:
        area_list = []

        area = Area.query.all()

        for item in area:
            area_list.append(item.to_dict())

        return jsonify(status=RET.OK, errmsg="OK", data=area_list)

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status=RET.DBERR, errmsg="获取地区失败")

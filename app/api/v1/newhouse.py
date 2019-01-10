from app.common import constants
from flask import current_app
from flask import g
from flask import render_template, jsonify
from flask import request

from app import db
from app.common.image_storage import image_storage
from app.common.response_code import RET
from app.models import House, Area
from . import api



@api.route("/v1/newhouse", methods=["POST"])
def house_index():

    # 1.获取参数
    user_id = g.user_id
    title = request.json.get("title")
    price = request.json.get("price")
    area_id = request.json.get("area_id")
    address = request.json.get("address")
    room_count = request.json.get("room_count")
    acreage = request.json.get("acreage")
    unit = request.json.get("unit")
    capacity = request.json.get("capacity")
    beds = request.json.get("beds")
    deposit = request.json.get("deposit")
    min_days = request.json.get("min_days")
    max_days = request.json.get("max_days")
    facility = request.json.get("facility")

    # 2. 校验参数,为空校验
    if not all([title,price,area_id, address,room_count,acreage,unit,capacity,beds,deposit,min_days,max_days,facility]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不全")

    # 3.判断城区id是否存在
    try:
        area = Area.query.get(area_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")

    if area is None:
        return jsonify(errno=RET.NODATA, errmsg="城区信息有误")

    # 4. 创建房源对象,设置属性
    house = House()
    house.user_id = user_id
    house.title = title
    house.price = price
    house.area_id = area_id
    house.address = address
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.beds = beds
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days

    # 4. 保存到数据
    try:
        db.session.add(house)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="房源发布失败")

    # 5. 返回响应
    return  render_template('house/newhouse.html',errmsg="发布成功")


@api.route("/new/houses/image", methods=["POST"])
def save_house_image():

    house_image = request.files.get("house_image")

    # 1. 校验参数,为空校验
    if not house_image:
        return jsonify(errno=RET.PARAMERR,errmsg="图片不能为空")

    # 2. 上传图像,判断图片是否上传成功
    try:
        #读取图片为二进制,上传图片
        image_name =  image_storage(house_image.read())

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR,errmsg="七牛云异常")

    if not image_name:
        return jsonify(errno=RET.NODATA,errmsg="图片上传失败")

    # 3. 将图片设置到用户对象
    g.user.house_image_url = image_name

    # 4. 返回响应
    data = {
        "house_image_url":constants.QINIU_DOMIN_PREFIX + image_name
    }

    return jsonify(errno=RET.OK, errmsg="OK", data=data)

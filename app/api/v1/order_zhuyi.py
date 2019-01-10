from flask import current_app
from flask import g
from flask import render_template, jsonify
from flask import request

from app import db
from app.common.common import user_login_data
from app.common.response_code import RET
from app.models import Order, House, User
from . import api


# 房客获取我的订单
# 房东获取客户订单
# URL：/api/orders
# 是否需要登录:是
# 请求方式：GET
# 请求参数：
# | 参数名  | 必选  | 类型  | 说明                                   |
# | role   | true | str  | 角色类型：【custom: 房客，landlord：房东】 |
# 返回结果
#     "data":
#          Order:                               订单列表
#             "order_id": 1,                    订单编号
#             "ctime": "2017-11-14 09:59:35",   订单创建时间
#             "start_date": "2017-11-14",       入住时间
#             "end_date": "2017-11-15",         离开时间
#             "days": 2,                        入住天数
#             "amount": 1000,                   合计
#             "status": "COMPLETE",             订单状态
#             "comment": "哎哟不错哟"             评价内容或拒单原因
#          House:                               房屋
#             "title": "555"                    房屋标题
#             "img_url": "",                    房屋图片
#     "errmsg": "OK",                           错误信息
#     "errno": "0"                              错误编号
@api.route('/orders')
@user_login_data
def my_orders():
    # 判断用户是否登录
    if not g.user:
        return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")
    # 获取参数
    role = request.args.get("role")
    # 获取g变量中的user
    user = g.user
    # 参数校验，为空校验
    if not all([user, role]):
        return jsonify(errno=RET.NODATA, errmsg="参数不全")
    # 判断请求类型
    # 我的订单
    if role == 'custom':
        # 返回我的订单
        try:
            my_orders = Order.query.filter(Order.user_id == user.id).order_by(Order.id.desc()).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="查询订单失败")
        # 判断查询结果是否为空
        if not my_orders:
            return render_template('order_zhuyi/orders.html',data=None)
        # 数据转换为字典
        my_order_list = []
        for order in my_orders:
            my_order_list.append(order.to_dict())
        # 返回数据，渲染页面
        data = {
            "my_order_list": my_order_list
        }
        return render_template('order_zhuyi/orders.html', data=data)
    # 客户订单
    elif role == 'landlord':
        # 判断当前用户类型，根据用户是否实名进行判断
        # 如果不是房东
        if not user.id_card:
            return jsonify(errno=RET.PARAMERR, errmsg="本功能需要实名认证")
            # 跳转到实名认证页面
            # return render_template()
        else:
            # 用户是否有出租房间
            # 如果无房间
            if not user.houses:
                return jsonify(errno=RET.NODATA, errmsg="你还未发布房源")
            # 创建该用户的房间id列表
            house_id_list = []
            # 循环遍历出house_id
            for house in user.houses:
                house_id_list.append(house.id)
            # 返回客户订单列表
            try:
                other_orders = Order.query.filter(Order.house_id.in_(house_id_list)).order_by(Order.id.desc()).all()
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(errno=RET.DBERR, errmsg="查询订单失败")
            # 如果查询到订单列表为空
            if not other_orders:
                return jsonify(errno=RET.NODATA, errmsg="暂时没有订单")
            # 数据转换为字典
            other_orders_list = []
            for other_order in other_orders:
                other_orders_list.append(other_order.to_dict())
            # 返回数据，渲染页面
            data = {
                "other_orders_list": other_orders_list
            }
            return render_template('order_zhuyi/lorders.html', data=data)


# 房客评论订单
# URL /api/orders/comment
# 是否需要登录 是
# 请求方式 PUT
# 请求参数
# | 参数名    | 必选  | 类型  | 说明     |
# | comment  | true | str  | 评论内容  |
# | order_id | true | int  | 订单号   |
# 返回结果
#    "errno": "0",      错误编号
#    "errmsg": "OK"     错误信息
@api.route('/orders/comment', methods=['PUT'])
@user_login_data
def orders_comment():
    # 判断用户是否登录
    if not g.user:
        return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")
    # 获取参数
    order_id = request.json.get("order_id")
    comment = request.json.get("comment")
    # 校验参数
    if not all([order_id, comment]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不全")
    # 查询订单信息
    try:
        order = Order.query.filter(Order.id == order_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询订单失败")
    # 订单不存在
    if not order:
        return jsonify(errno=RET.NODATA, errmsg="订单不存在")
    # 订单的状态应为待评价
    if not order.status == "WAIT_COMMENT":
        return jsonify(errno=RET.DATAERR, errmsg="订单状态错误")
    # 评论
    try:
        order.comment = comment
        order.status = 'COMPLETE'
        db.session.commit()
        return jsonify(errno=RET.OK, errmsg="评论成功")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="评论失败")


# 接单和拒单
# URL：/api/orders/action
# 是否需要登录：是
# 请求方式：PUT
# 请求参数
# | 参数名    | 必选  | 类型  | 说明                                  |
# | action   | true  | str  | 操作类型：【accept: 接单，reject：拒单】 |
# | order_id | true  | int  | 订单号                                |
# | reason   | false | str  | 拒单时，需要填写拒单原因                 |
# 返回结果
#    "errno": "0",
#    "errmsg": "OK"
@api.route('/orders/action', methods=['PUT'])
@user_login_data
def other_orders():
    # 判断用户是否登录
    if not g.user:
        return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")
    # 获取参数
    action = request.json.get("action")
    order_id = request.json.get("order_id")
    reason = request.json.get("reason")
    # 校验参数，为空校验
    if not all([action, order_id, reason]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不全")
    # 校验操作参数
    if not (action in ['accept', 'reject']):
        return jsonify(errno=RET.PARAMERR, errmsg="操作类型有误")
    # 查询订单信息
    try:
        order = Order.query.filter().first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="查询订单失败")
    # 判断订单是否存在
    if not order:
        return jsonify(errno=RET.NODATA, errmsg="订单不存在")
    # 判断操作类型
    try:
        # 接单
        if action == "accept":
            order.status = 'WAIT_COMMENT'
        # 拒单
        elif action == "reject":
            order.status = 'REJECTED'
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="操作失败")
    return jsonify(errno=RET.OK, errmsg="操作成功")


# @api.route('/<path:file_name>')
# def order_test(file_name):
#     file_name = "html/" + file_name
#     return current_app.send_static_file(file_name)


# 用户登录测试
def userLoginTest(userid):
    try:
        user = User.query.get(userid)
        g.user = user
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库连接失败")

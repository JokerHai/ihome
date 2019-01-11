#个人中心修改
from app import db
from app.common.response_code import RET
from ..v1 import api
from flask import render_template,request, jsonify,g
from app.common.common import user_login_data


@api.route('/profile_view',methods = ['GET', 'POST'])
@user_login_data
def profile_view():

    # 判断用户是否登录
    if not  g.user:
        return jsonify(errno=RET.NODATA,errmsg="用户未登录")

    # 判断请求方式,如果是git请求,携带用户数据,渲染页面
    if request.method == "GET":
        return render_template("profile/profile.html",user_info=g.user.to_dict())

    # 如果是post请求,获取参数
    name = request.json.get("name")



    # 检验参数,为空校验
    if not all([name]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不全")

    # 修改用户的数据
    g.user.name = name

    db.session.commit()

    # 返回响应
    return jsonify(errno=RET.OK, errmsg="修改成功")


@api.route('/profile_view',methods = ['POST'])
@user_login_data
def pic_info():
    # 判断用户是否登录
    if not g.user:
        return jsonify(errno=RET.NODATA, errmsg="用户未登录")



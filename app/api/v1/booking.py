import time
from flask import current_app,render_template, jsonify
from flask import request
from flask_login import current_user

from app.common.response_code import RET
from ..v1 import api

@api.route('/v1.0/orders', methods=["GET",'POST'])
def booking():
    if not current_user.is_authenticated:
        return jsonify(errno=RET.USERERR,errmsg="用户未登录")
    dict_data=request.json
    house_id=int(dict_data.get("house_id"))
    start_date=time.strptime(dict_data.get("start_date"),"%Y-%m-%d")
    end_date=time.strptime(dict_data.get("end_date"),"%Y-%m-%d")
    if not all([house_id,start_date, end_date]):
        return jsonify(errno=RET.NODATA,errmsg="参数不全")








    return render_template("booking/booking.html")




from flask import g, jsonify
from flask import redirect
from flask_login import current_user

from app.common.response_code import RET
from ..v1 import api
from  flask import  render_template

@api.route('/user_index',methods = ['GET','POST'])
def user_index():

    # if not current_user.is_authenticated:
    #      return redirect("/")
    # data = {
    #     "users_api":users.to_dict()
    # }

    data = {
            "name":'张三',
            "iphone":'15011390890',
            'avatar_url':'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1547118492715&di=93f5e44e9202ebe1f7b118be8fecebc0&imgtype=0&src=http%3A%2F%2Fwww.005.tv%2Fuploads%2Fallimg%2F160126%2F9-160126162633517.jpg'
           }
    #return jsonify(errno=RET.DBERR, errmsg="获取个人首页失败")
    return render_template('users/user_index.html',info = data)

#个人中心修改
from ..v1 import api
from flask import render_template

@api.route('/profile_view',methods = ['GET'])
def profile_view():

    return render_template('profile/profile.html')
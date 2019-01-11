from flask_login import login_required, current_user
from ..v1 import api
from  flask import  render_template
@login_required
@api.route('/user_index',methods = ['GET','POST'])
def user_index():
    data = current_user.to_dict()
    return render_template('users/user_index.html',info = data)

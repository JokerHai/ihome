# -*- coding: utf-8 -*-
#登录组件
# @Author  : joker
# @Date    : 2019-01-03
from flask_wtf import FlaskForm
from wtforms.validators import  ValidationError
from ..models import User

class RegistrationForm(FlaskForm):

    # register_mobile = StringField(_name = 'abc',validators=[
    #     DataRequired(),length(1,11),
    #     Regexp('1[3-9]\d{9}',0,
    #            'mobile must have number underscores'
    #            )])
    # password = PasswordField('password',validators=[
    #     DataRequired(),length(6,12)
    # ])
    # submit = SubmitField('register')
    @staticmethod
    def validate_mobile(field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('mobile already in use.')
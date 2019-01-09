# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-27

from  flask import  Blueprint

auth = Blueprint('auth',__name__)

from . import views


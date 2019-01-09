# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2018-12-28
from ..v1 import api

@api.route('/')
def index():
    return 'This Is Project Api'
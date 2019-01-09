# -*- coding: utf-8 -*-
# 公共方法
# @Author  : joker
# @Date    : 2019-01-02
import re

# 效验手机号
def check_mobile(mobile):
    if mobile is not None:
        if re.match("1[3-9]\d{9}", mobile) is not None:
            return True
        else:
            return False
    else:
        return False



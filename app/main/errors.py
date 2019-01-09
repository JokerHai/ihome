# -*- coding: utf-8 -*-
# 错误页
# @Author  : joker
# @Date    : 2018-12-27
from flask import request, jsonify, render_template

from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404

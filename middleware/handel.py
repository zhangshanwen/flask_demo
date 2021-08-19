import logging

from flask import request

from tools import render


def base_request():
    if request.method in ["POST", "PUT", "PATCH"]:
        if not request.json:
            return render.render_failed({}, msg="request params err")
    # request_ip = request.environ.get("HTTP_X_FORWARD_FOR")  # 请求ip nginx 需配置@1
    # # 黑名单/白名单 设置
    # if request_ip == "127.0.0.1":
    #     logging.info("request_ip", request_ip)
    #     render.render_failed({
    #         "request_ip": request_ip, }, msg="IP restricted access")

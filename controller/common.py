import functools

from flask import request

from tools import render, log


def check_request(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if request.method in ["POST", "PUT"]:
            if not request.json:
                log.logger.info("request_params", request.json)
                return render.render_failed({"request_params": request.json}, msg="request params err")
        # request_ip = request.environ.get("HTTP_X_FORWARD_FOR")  # 请求ip nginx 需配置@1
        # # 黑名单/白名单 设置
        # if request_ip == "127.0.0.1":
        #     log.logger.info("request_ip", request_ip)
        #     render.render_failed({
        #         "request_ip": request_ip, }, msg="IP restricted access")
        return func(*args, **kwargs)

    return inner

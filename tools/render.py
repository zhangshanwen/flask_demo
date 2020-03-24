from time import time

from flask import jsonify

from . import code


def render(status, msg, data):
    result = {
        "status": status,
        "msg": msg,
        "server_time": time(),
        "data": data,
        "request_id": code.generate_uuid()
    }
    return jsonify(result)


def render_success(data, msg="ok"):
    return render(1, msg, data)


def render_failed(data, msg="failed"):
    return render(0, msg, data)

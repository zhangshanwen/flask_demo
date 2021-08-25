from time import time
import logging

from flask import request, jsonify
from . import code

default_page = 1
default_page_size = 20
default_sort = 0  # 0 desc 1 asc
default_order = "id"


def get_page():
    try:
        page = int(request.args.get("page", default_page))
        page_size = int(request.args.get("page_size", default_page_size))
        sort = int(request.args.get("sort", default_sort))
        order = request.args.get("order", default_order)
    except Exception as e:
        logging.error(e)
        page = default_page
        page_size = default_page_size
        sort = default_sort
        order = default_order
    return page, page_size, (page - 1) * page_size, sort, order


def render(status, msg, data):
    result = {
        "status": status,
        "msg": msg,
        "server_time": int(time()),
        "data": data,
        "request_id": code.generate_uuid()
    }
    return jsonify(result)


def render_success(data=None, msg="ok", status_code=200):
    if data is None:
        data = {}
    return render(1, msg, data), status_code


def render_failed(data=None, msg="failed", status_code=400):
    if data is None:
        data = {}
    return render(0, msg, data), status_code

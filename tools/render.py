from time import time
import logging

from flask import request, jsonify
from sqlalchemy import desc

from . import code
from .bind import to_json

default_page = 1
default_page_size = 20
default_sort = 0  # 0 desc 1 asc
default_order = "id"


class Pagination:
    def __init__(self):
        try:
            self.page = int(request.args.get("page", default_page))
            self.page_size = int(request.args.get("page_size", default_page_size))
            self.sort = int(request.args.get("sort", default_sort))
            self.order = request.args.get("order", default_order)
        except Exception as e:
            logging.error(e)
            self.page = default_page
            self.page_size = default_page_size
            self.sort = default_sort
            self.order = default_order
        if self.sort:
            self.order_by = desc(self.order)
        else:
            self.order_by = self.order
        self.offset = (self.page - 1) * self.page_size

    def to_dict(self):
        return to_json(self, ignoreList=["order_by", "offset"])


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

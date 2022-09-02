import logging

from flask import request
from copy import deepcopy
import enums

_sa_instance_state = '_sa_instance_state'


def bind_json(params):
    return set_params(params, request.json)


def set_params(params, args):
    try:
        for k, v in args.items():
            if hasattr(params, k):
                v = type(getattr(params, k))(v)
                setattr(params, k, v)
    except Exception as e:
        logging.error(e)
        return enums.param_err


def bind_param(params):
    if request.method.upper() in ["POST", "PUT", "PATCH"]:
        return set_params(params, request.json)
    return set_params(params, request.args)


def to_json(orm_object, need_list: list = None, ignore_list: list = None) -> dict:
    items = deepcopy(orm_object.__dict__)
    if _sa_instance_state in items:
        items.pop("_sa_instance_state")
    if need_list:
        items = {k: v for k, v in items.items() if k in need_list}
    elif ignore_list:
        for ignore in ignore_list:
            if ignore in items:
                items.pop(ignore)
    return items

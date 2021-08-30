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
    if request.method in ["POST", "PUT", "PATCH"]:
        return set_params(params, request.json)
    return set_params(params, request.args)


def to_json(ormObject, needList: list = None, ignoreList: list = None) -> dict:
    items = deepcopy(ormObject.__dict__)
    if _sa_instance_state in items:
        items.pop("_sa_instance_state")
    if needList:
        items = {k: v for k, v in items.items() if k in needList}
    elif ignoreList:
        for ignore in ignoreList:
            if ignore in items:
                items.pop(ignore)
    return items

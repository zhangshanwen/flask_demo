import logging

from flask import request, session
import enums
from tools import render
from tools.code import decode_auth_token


def jwt_request():
    authorization = request.headers.get(enums.Authorization)
    if not authorization:
        return render.render_failed(msg=enums.auth_error)
    user_id = decode_auth_token(authorization)
    if not user_id:
        return render.render_failed(msg=enums.auth_invalid)
    # read from session or redis
    user = session.get(str(user_id))
    if not user:
        return render.render_failed(msg=enums.auth_invalid)

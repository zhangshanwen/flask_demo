import logging

from flask import request, session, g
import enums
from tools import render
from tools.code import decode_auth_token


def jwt_request():
    authorization = request.headers.get(enums.Authorization)
    if not authorization:
        return render.render_failed(msg=enums.auth_error, status_code=401)
    user_id = decode_auth_token(authorization)
    if not user_id:
        return render.render_failed(msg=enums.auth_invalid, status_code=401)
    # read from session or redis
    user = session.get(str(user_id))
    if not user:
        return render.render_failed(msg=enums.auth_invalid, status_code=401)
    setattr(g, enums.current_user, user)

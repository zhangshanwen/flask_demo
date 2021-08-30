import time
from flask import request, current_app, session
from sqlalchemy import or_

from . import login_bp
import enums
from tools.render import render_failed, render_success, to_json
from tools import code
from libs.db import Db
from model.user import User
from params.login import UserLoginParam


@login_bp.route("/api/user/login", methods=["POST"])
def login_view():
    db = Db()
    param = UserLoginParam()
    if err := param.check_param():
        return render_failed(msg=err)
    user = db.query(User).filter(or_(User.mobile == param.key, User.user_name == param.key), User.password ==
                                 code.generate_md5(current_app.config.get("SALT") + param.password)).first()
    if not user:
        return render_failed("", enums.account_password_error)
    user.last_login_time = int(time.time())
    res = to_json(user, ignoreList=["updated_time", "created_time"])
    db.commit()
    session[str(user.id)] = res

    result = {
        "Authorization": code.encode_auth_token(user.id)
    }
    result.update(res)
    return render_success(result)

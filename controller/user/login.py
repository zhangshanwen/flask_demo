import time
from flask import request, current_app, session
from sqlalchemy import or_

from . import login_bp
import enums
from tools.render import render_failed, render_success
from tools import code
from libs import ts, db
from model.user import User


@login_bp.route("/api/user/login", methods=["POST"])
def login_view():
    key = request.json.get("key")
    password = request.json.get("password")
    if not all([key, password]):
        return render_failed("", enums.param_err)
    user = db.query(User).filter(or_(User.mobile == key, User.user_name == key), User.password ==
                                 code.generate_md5(current_app.config.get("SALT") + password)).first()
    if not user:
        return render_failed("", enums.account_password_error)
    user.last_login_time = int(time.time())
    db.commit()
    session[str(user.id)] = {
        "user_name": user.user_name,
        "mobile": user.mobile,
        "last_login_time": user.last_login_time
    }
    return render_success({"Authorization": code.encode_auth_token(user.id)})

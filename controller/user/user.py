from flask import request, current_app

from . import login_bp
import enums
from tools.render import render_failed, render_success
from tools import code
from libs import ts, db
from model.user import User


@login_bp.route("/api/user", methods=["POST"])
def user_view():
    user_name = request.json.get("user_name")
    password = request.json.get("password")
    mobile = request.json.get("mobile")
    # sms_code = request.json.get("sms_code")
    if not all([user_name, password, mobile]):
        return render_failed("", enums.param_err)
    # ts_code = ts.get(enums.register_sms_key + mobile)
    # if not ts_code:
    #     return render_failed("", enums.sms_code_valid)
    # if ts_code.decode() != sms_code:
    #     return render_failed("", enums.sms_code_err)
    exist_user = db.query(User).filter(User.mobile == mobile).first()
    if exist_user:
        return render_failed("", enums.mobile_exist)
    exist_user = db.query(User).filter(User.user_name == user_name).first()
    if exist_user:
        return render_failed("", enums.username_exist)
    user = User(user_name=user_name, mobile=mobile,
                password=code.generate_md5(current_app.config.get("SALT") + password))
    db.add(user)
    db.commit()
    return render_success()

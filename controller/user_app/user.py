from flask import request, current_app

from . import login
import enums
from controller.common import check_request
from tools.render import render_failed, render_success
from tools import sms, code
from libs import ts, session
from model.user import User


@login.route("/api/sms", methods=["POST"])
@check_request
def sms():
    # sms_key: sms_key  register/login/reset password
    mobile = request.json.get("mobile")
    sms_key = request.json.get("sms_key")
    if not all([mobile, sms_key]):
        return render_failed("", enums.param_err)
    if ts.get(mobile + sms_key):
        return render_failed("", enums.sms_repetition)
    sms_code = code.generate_digital_code()
    ts.setex(mobile + sms_key, sms_code, 120)
    sms.send_msg(mobile, sms_code)


@login.route("/api/user/register", methods=["POST"])
@check_request
def register():
    user_name = request.json.get("user_name")
    password = request.json.get("password")
    mobile = request.json.get("mobile")
    sms_code = request.json.get("sms_code")
    if not all([user_name, password, mobile, sms_code]):
        return render_failed("", enums.param_err)
    # ts_code = ts.get(enums.register_sms_key + mobile)
    # if not ts_code:
    #     return render_failed("", enums.sms_code_valid)
    # if ts_code.decode() != sms_code:
    #     return render_failed("", enums.sms_code_err)
    u = User(user_name=user_name, mobile=mobile,
             password=code.generate_md5(current_app.config.get("SALT") + password))
    session.add(u)
    session.commit()
    return render_success({"X-AUTH-TOKEN": code.encode_auth_token(u.id)})

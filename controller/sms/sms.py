from flask import request, current_app
from flask.views import MethodView

from sqlalchemy import or_

from . import sms_bp
import enums
from tools.render import render_failed, render_success
from tools import sms, code
from libs import ts, db


@sms_bp.route("/api/sms", methods=["POST"])
def sms_view():
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

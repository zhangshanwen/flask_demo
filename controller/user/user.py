import time

from flask import request, current_app, session, g

from . import login_bp, users_bp
import enums
from tools.render import render_failed, render_success
from tools import code
from libs import ts, db
from model.user import User


@login_bp.route("/api/user", methods=["POST"])
def register_view():
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
    exist_user = db.query(User).filter(User.mobile == mobile).count()
    if exist_user:
        return render_failed("", enums.mobile_exist)
    exist_user = db.query(User).filter(User.user_name == user_name).count()
    if exist_user:
        return render_failed("", enums.username_exist)
    user = User(user_name=user_name, mobile=mobile,
                password=code.generate_md5(current_app.config.get("SALT") + password))
    db.add(user)
    db.commit()
    return render_success()


@users_bp.route("/api/user/<user_id>", methods=["PUT", 'DELETE'])
def user_view(user_id):
    if request.method == "PUT":
        return user_edit(user_id)
    else:
        return user_delete(user_id)


def user_edit(user_id):
    user_name = request.json.get("user_name")
    mobile = request.json.get("mobile")
    if not all([user_name, mobile]):
        return render_failed("", enums.param_err)
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return render_failed("", enums.error_id)
    exist_user = db.query(User).filter(User.mobile == mobile).filter(User.id != user_id).count()
    if exist_user:
        return render_failed("", enums.mobile_exist)
    exist_user = db.query(User).filter(User.user_name == user_name).filter(User.id != user_id).count()
    if exist_user:
        return render_failed("", enums.username_exist)
    user.user_name = user_name
    user.mobile = mobile
    user.updated_time = int(time.time())
    db.commit()
    if str(user_id) in session.keys():
        session.pop(str(user_id))
    return render_success({
        "id": user.id, "user_name": user.user_name, "mobile": user.mobile,
        "last_login_time": user.last_login_time,
        "created_time": user.created_time, "updated_time": user.created_time,
    })


def user_delete(user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return render_failed("", enums.error_id)
    db.delete(user)
    db.commit()
    if str(user_id) in session.keys():
        session.pop(str(user_id))
    return render_success()


@users_bp.route("/api/user/password/reset/<user_id>", methods=["GET"])
def user_reset_password(user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return render_failed("", enums.error_id)
    user.password = code.generate_md5(current_app.config.get("SALT") + current_app.config.get("DEFAULT_PASSWORD"))
    db.commit()
    if str(user_id) in session.keys():
        session.pop(str(user_id))
    return render_success()


@users_bp.route("/api/user/password", methods=["PUT"])
def user_update_password():
    password = request.json.get("password")
    if not password:
        return render_failed("", enums.param_err)
    user = g.get(enums.current_user)
    password = code.generate_md5(current_app.config.get("SALT") + password)
    if user.get("password") == password:
        return render_failed("", enums.password_not_the_same)
    db.query(User).filter(User.id == user.get("id")).update(
        {
            User.password: password
        })
    db.commit()
    if str(user.get("id")) in session.keys():
        session.pop(str(user.get("id")))
    return render_success()


@users_bp.route("/api/user/logout", methods=["DELETE"])
def logout():
    user = g.get(enums.current_user)
    if str(user.get("id")) in session.keys():
        session.pop(str(user.get("id")))
    return render_success()

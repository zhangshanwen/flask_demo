import time

from flask import request, current_app, session, g

from . import login_bp, users_bp
import enums
from tools.render import render_failed, render_success
from tools import code
from libs.db import Db
from model.user import User
from params.user import UserSaveParam, UserEditParam, UserPasswordParam


@login_bp.route("/api/user", methods=["POST"])
def register_view():
    db = Db()
    param = UserSaveParam()
    if err := param.check_param():
        return render_failed(msg=err)
    # ts_code = ts.get(enums.register_sms_key + mobile)
    # if not ts_code:
    #     return render_failed(msg= enums.sms_code_valid)
    # if ts_code.decode() != sms_code:
    #     return render_failed(msg=enums.sms_code_err)
    exist_user = db.query(User).filter(User.mobile == param.mobile).count()
    if exist_user:
        return render_failed(msg=enums.mobile_exist)
    exist_user = db.query(User).filter(User.user_name == param.user_name).count()
    if exist_user:
        return render_failed(msg=enums.username_exist)
    param.password = code.generate_md5(current_app.config.get("SALT") + param.password)
    db.create_one(User, param)
    if db.err:
        return render_failed(msg=db.err)
    return render_success()


@users_bp.route("/api/user/<user_id>", methods=["PUT", 'DELETE'])
def user_view(user_id):
    if request.method == "PUT":
        return user_edit(user_id)
    else:
        return user_delete(user_id)


def user_edit(user_id):
    db = Db()
    param = UserEditParam()
    if err := param.check_param():
        return render_failed(msg=err)
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return render_failed(msg=enums.error_id)
    exist_user = db.query(User).filter(User.mobile == param.mobile).filter(User.id != user_id).count()
    if exist_user:
        return render_failed(msg=enums.mobile_exist)
    exist_user = db.query(User).filter(User.user_name == param.user_name).filter(User.id != user_id).count()
    if exist_user:
        return render_failed(msg=enums.username_exist)
    db.update_one(User, user_id, param)
    if db.err:
        return render_failed(msg=db.err)
    if str(user_id) in session.keys():
        session.pop(str(user_id))
    return render_success(db.to_json(ignoreList=["password"]))


def user_delete(user_id):
    db = Db()
    db.delete_one(User, user_id)
    if db.err:
        return render_failed(msg=db.err)
    if str(user_id) in session.keys():
        session.pop(str(user_id))
    return render_success()


@users_bp.route("/api/user/password/reset/<user_id>", methods=["GET"])
def user_reset_password(user_id):
    db = Db()
    param = UserPasswordParam()
    if err := param.check_param():
        return render_failed(msg=err)
    param.password = code.generate_md5(current_app.config.get("SALT") + param.password)
    db.update_one(User, user_id, param)
    if db.err:
        return render_failed(msg=db.err)
    return render_success()


@users_bp.route("/api/user/password", methods=["PUT"])
def user_update_password():
    db = Db()
    param = UserPasswordParam()
    if err := param.check_param():
        return render_failed(msg=err)
    user = g.get(enums.current_user)
    param.password = code.generate_md5(current_app.config.get("SALT") + param.password)
    if user.get("password") == param.password:
        return render_failed("", enums.password_not_the_same)
    db.update_one(User, user.get("id"), param)
    if db.err:
        return render_failed(msg=db.err)
    if str(user.get("id")) in session.keys():
        session.pop(str(user.get("id")))
    return render_success()


@users_bp.route("/api/user/logout", methods=["DELETE"])
def logout():
    user = g.get(enums.current_user)
    if str(user.get("id")) in session.keys():
        session.pop(str(user.get("id")))
    return render_success()

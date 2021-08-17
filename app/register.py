# register  blue print


def register(app):
    # need import your view  example user
    from controller.user import login_bp, users_bp, user, users, login
    from controller.sms import sms_bp, sms
    app.register_blueprint(sms_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(users_bp)

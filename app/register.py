# register  blue print


def register(app):
    # need import your view  example user
    from controller.user_app import login, user
    app.register_blueprint(login)

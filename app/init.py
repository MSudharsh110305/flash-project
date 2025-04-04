from flask import Flask
from .extensions import db, migrate, login_manager, socketio
from .auth import auth as auth_blueprint
from .projects import projects as projects_blueprint

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.inti_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(projects_blueprint, url_prefix='/projects')

    return app
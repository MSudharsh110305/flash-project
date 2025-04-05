from flask import Flask, render_template
from .extensions import db, migrate, login_manager, socketio
from config import Config  

def create_app(config_class=Config):  
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .projects import projects as projects_blueprint
    app.register_blueprint(projects_blueprint, url_prefix='/projects')

    @app.route('/')
    def index():
        return "Welcome to the Project Management Platform!"

    return app

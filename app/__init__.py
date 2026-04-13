from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import views
    return app

    from .views import bp
    app.register_blueprint(bp)

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    csrf = CSRFProtect(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import bp
    app.register_blueprint(bp, url_prefix='/api/v1')

    return app

   





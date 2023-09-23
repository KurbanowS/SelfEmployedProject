from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):    
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from main.developers import bp as developer_bp
    app.register_blueprint(developer_bp)

    from main.designers import bp as designer_bp
    app.register_blueprint(designer_bp)

    return app


# from main.developers import routes, models
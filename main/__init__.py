from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_msearch import Search
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
# search = Search()
login.login_view = 'AD.admin_login'

def create_app(config_class=Config):    
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    # search.init_app(app)
    # search.create_index(update=True)
    
    from main.developers import bp as developer_bp
    app.register_blueprint(developer_bp)

    from main.designers import bp as designer_bp
    app.register_blueprint(designer_bp)

    from main.errors import bp as error_bp
    app.register_blueprint(error_bp)

    from main.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    return app


# from main.developers import routes, models
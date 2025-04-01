from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .models import Usuario

    # with app.app_context():
    #     db.create_all()
    
    migrate.init_app(app, db)
    
    # Importa e registra as rotas
    from .routes import main
    app.register_blueprint(main)

    return app

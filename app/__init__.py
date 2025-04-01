from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')  # Carrega configurações do config.py

    # Importa e registra as rotas
    from .routes import main
    app.register_blueprint(main)

    return app

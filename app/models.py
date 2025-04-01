from . import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(15), unique=True, nullable=False)
    nome = db.Column(db.String(80), nullable=False)
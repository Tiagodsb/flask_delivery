from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Usuario

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/registro')
def registro():
    return render_template('registro.html')

@main.route('/criar_conta', methods=['POST'])
def criar_conta():
    tel = request.form['telefone']
    nome = request.form['nome']

    novo_usuario = Usuario(numero=tel, nome=nome)
    db.session.add(novo_usuario)
    db.session.commit()
    return render_template('login.html')

@main.route('/entrar')
def entrar():
    return render_template('login.html')

@main.route('/usuario')
def usuario():
    return render_template('usuario.html')

@main.route('/autorizacao', methods=['POST'])
def autorizacao():
    tel = request.form['telefone']
    nome = request.form['nome']    
    usuario = Usuario.query.filter_by(numero=tel, nome=nome).first()
    if not usuario:
        return redirect(url_for('main.entrar'))
    
    return redirect(url_for('main.usuario'))

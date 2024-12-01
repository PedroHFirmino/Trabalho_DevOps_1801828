
from flask import request, jsonify
from app.models import db, Aluno

def init_app(app):
    @app.route('/cadastro', methods=['POST'])
    def cadastro():
        data = request.get_json()
        nome = data.get('nome')
        ra = data.get('ra')

       
        novo_aluno = Aluno(nome=nome, ra=ra)
        db.session.add(novo_aluno)
        db.session.commit()

        return jsonify({"message": "Aluno cadastrado com sucesso!"}), 201


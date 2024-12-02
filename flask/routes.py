from flask import Flask, request, jsonify
from models import db, Aluno

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:@db/cadastro_alunos'
db.init_app(app)

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.get_json()
    novo_aluno = Aluno(nome=data['nome'], ra=data['ra'])
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno cadastrado com sucesso!'}), 201

from flask import Flask
from app.routes import main

app = Flask(__name__)  # Corrigido para __name__
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@db/cadastro_alunos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrigido para TRACK_MODIFICATIONS

# Importa as rotas
app.register_blueprint(main)

if __name__ == "__main__":  # Corrigido para __name__
    app.run(host='0.0.0.0', port=5000)

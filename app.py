from flask import Flask
from app.routes import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/alunos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Importa rotas
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

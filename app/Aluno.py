
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"<Aluno {self.nome} - {self.ra}>"

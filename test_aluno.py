import unittest
from app import app, db, Aluno

class TestAluno(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def test_cadastrar_aluno(self):
        response = self.app.post('/alunos', json={'nome': 'João', 'ra': '12345'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Aluno cadastrado com sucesso!', response.get_data(as_text=True))

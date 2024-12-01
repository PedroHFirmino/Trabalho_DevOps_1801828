import unittest
from app import app, db
from app import Aluno  

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
        cls.app = app.test_client()
        cls.app_context = app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bem-vindo', response.data)  

    def test_cadastro_aluno(self):
        
        novo_aluno = Aluno(nome="João Silva", ra="123456")
        db.session.add(novo_aluno)
        db.session.commit()

        aluno = Aluno.query.filter_by(ra="123456").first()
        self.assertIsNotNone(aluno)
        self.assertEqual(aluno.nome, "João Silva")

    def test_cadastro_endpoint(self):
        
        response = self.app.post('/cadastro', json={"nome": "Maria Souza", "ra": "654321"})
        self.assertEqual(response.status_code, 200)

        aluno = Aluno.query.filter_by(ra="654321").first()
        self.assertIsNotNone(aluno)
        self.assertEqual(aluno.nome, "Maria Souza")


if __name__ == '__main__':
    unittest.main()

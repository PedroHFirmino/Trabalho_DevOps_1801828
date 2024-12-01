from flask import Flask
from app.models import db 
from app.routes import init_app

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@db/cadastro_alunos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  

from app.routes import init_app  
init_app(app)

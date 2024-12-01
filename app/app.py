from flask import Flask
from app.routes import main

app = Flask(name)
app.config['SQLALCHEMYDATABASEURI'] = 'mysql+pymysql://root:password@db/alunosdb'
app.config['SQLALCHEMYTRACK_MODIFICATIONS'] = False


app.register_blueprint(main)

if __name == "__main":
    app.run(host='0.0.0.0', port=5000)
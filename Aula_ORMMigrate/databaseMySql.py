from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Para obter detales sobre a URI consulte o link
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userbd:Teste#1234@localhost:3306/BD_ORM'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

dbMySql = SQLAlchemy(app)

class PetAdocao(dbMySql.Model):
    id = dbMySql.Column(dbMySql.Integer, primary_key=True)
    apelido = dbMySql.Column(dbMySql.String(500), unique=True)
    perfil = dbMySql.Column(dbMySql.String(200))
    dataregistro = dbMySql.Column(dbMySql.DateTime())
    castrado = dbMySql.Column(dbMySql.Boolean, default=True)
    responsavel = dbMySql.Column(dbMySql.String(200))
    contato = dbMySql.Column(dbMySql.String(100), nullable=True)

    def __init__(self,apelido, perfil, dataregistro, castrado, responsavel, contato):
        self.apelido = apelido
        self.perfil = perfil
        self.dataregistro = dataregistro
        self.castrado = castrado
        self.responsavel = responsavel
        self.contato = contato


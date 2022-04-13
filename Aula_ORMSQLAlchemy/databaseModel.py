# Setup para comunicar com o BD

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://userbd:Teste#1234@localhost:3306/BD_ORM'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# --------------

class PetAdocao(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    apelido = db.Column(db.String(60))
    perfil = db.Column(db.String(100))
    dataRegistro = db.Column(db.DateTime())
    castrado = db.Column(db.Boolean, default=True)
    responsavel = db.Column(db.String(100))
    contato = db.Column(db.String(100))

    def __init__(self, apelido, perfil, dataRegistro,castrado, responsavel,contato):
        self.apelido = apelido
        self.perfil = perfil
        self.dataRegistro = dataRegistro
        self.castrado = castrado
        self.responsavel = responsavel
        self.contato = contato
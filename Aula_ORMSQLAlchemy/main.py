
from databaseModel import db, PetAdocao

# ativar somente para testes
db.drop_all()
db.create_all()
#

toto = PetAdocao('Toto', 'nervoso, mas bricalhão', '2022-04-16', True, 'Ana Maria Braga', 'ana@gmail.com')
print(toto.apelido)
db.session.add(toto) # Adicionar o objeto na BD
db.session.commit()
print(f'ID: {toto.id}')

# Trabalhando com Lista
pets = [
    PetAdocao('Furação','docil','2022-04-10',True,'Ana Maria Braga','ana@gmail.com'),
    PetAdocao('Fofinho','bravo','2021-12-01',True,'Fausto Silva','fausto@gmail.com'),
    PetAdocao('Costelinha','docil','2020-11-11',False,'Pedro Bial','pedro@gmail.com')
]
print(pets)
print('>--- Adicionar a Lista no BD')

for pet in pets:
    print(f'Salvando: {pet.apelido} - {pet.responsavel}')
    db.session.add(pet)
db.session.commit()

# Consulta informações no BD

print('>--- Consultado os dados do Banco')

pets_db = db.session.query(PetAdocao).all()
for pet in pets_db:
    print(f'id: {pet.id} - {pet.apelido} - {pet.perfil} - {pet.contato}')

# Consultar apenas 1 registro no Banco
pet_found = PetAdocao.query.filter_by(id=4).first()
print(f'Localizou: {pet_found.id} - {pet_found.apelido}')

# Remover esse registro
print('Removendo registro id=4')
db.session.delete(pet_found)
db.session.commit()

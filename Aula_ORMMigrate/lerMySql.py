from databaseMySql import dbMySql, PetAdocao

print('--- Ler dados SALVOS no MySQL')

pets_db = dbMySql.session.query(PetAdocao).all()

for pet in pets_db:
    print(f'id: {pet.id} - {pet.apelido}')

dbMySql.session.close()
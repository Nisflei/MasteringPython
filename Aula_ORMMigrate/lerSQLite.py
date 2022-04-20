from databaseSqLite import dbLite, PetAdocao

print('--- Ler dados SALVOS no SQLITE')

pets_db = dbLite.session.query(PetAdocao).all()

for pet in pets_db:
    print(f'id: {pet.id} - {pet.apelido}')

dbLite.session.close()



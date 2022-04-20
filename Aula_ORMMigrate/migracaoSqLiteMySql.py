
## Passo 1: Carregar os dados de origem

from databaseSqLite import dbLite, PetAdocao

print('--- Ler dados SALVOS no SQLITE')

pets_dbLite = dbLite.session.query(PetAdocao).all()

for pet in pets_dbLite:
    print(f'id: {pet.id} - {pet.apelido}')

dbLite.session.close()

# Passo 2: Adicionar os PETS em memoria no Bando de Destino

from databaseMySql import dbMySql,PetAdocao

#--- executar para permitir LIMPAR o MySQL
dbMySql.drop_all()
dbMySql.create_all()
#-----

print()
print('--- Adicionando dados no MySQL ')

for pet in pets_dbLite:
    print(f'Adicionando: {pet.apelido}')
    dbMySql.session.add(PetAdocao(pet.apelido,
                                  pet.perfil,
                                  pet.dataregistro,
                                  pet.castrado,
                                  pet.responsavel,
                                  pet.contato))

dbMySql.session.commit()
from databaseSqLite import dbLite, PetAdocao
from datetime import datetime
#---- Para remontar sempre os dados
dbLite.drop_all()
dbLite.create_all()
#-----

pets = [
PetAdocao('Furacão', 'Dócil', datetime.strptime('2022-04-12','%Y-%m-%d'),True,'Ana Maria','ana@gmail.com'),
PetAdocao('Fofinho', 'Bravo', datetime.strptime('2021-12-01','%Y-%m-%d'),True,'Fausto','fausto@gmail.com'),
PetAdocao('Costelinha', 'Dócil', datetime.strptime('2020-11-11','%Y-%m-%d'),False,'Doug','doug@gmail.com')
]

for pet in pets:
    print(f'Adicionando: {pet.apelido}')
    dbLite.session.add(pet)

dbLite.session.commit()


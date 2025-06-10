#Instalar a biblioteca requests com o comando "pip install requests"
import requests
from pymongo import MongoClient

#1 - Estabelecendo conexão com o mongoDB local
client = MongoClient()
db = client['nobel'] #Criando o banco de dados Nobel

#2 - Importando dados em Documentos
for collection_name in ["prizes", "laureates"]:
    response = requests.get(f"http://api.nobelprize.org/v1/{collection_name[:-1]}.json")
    document = response.json()[collection_name]
    db[collection_name].insert_many(document)

#3 - Acessand coleções e contagem de documentos na coleção
prizes = db["prizes"]
laureates = db["laureates"]

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})
print(len_prizes)
print(len_laureates)
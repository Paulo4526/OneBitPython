#Primeiramente instalaremos a biblioteca mongo no python com o comando "pip install pymongo"
from pymongo import MongoClient

client = MongoClient() #Salvando as informações do cliente na variavel client
mydb = client.obcblog #Criando banco de dados com nome de obcblog
mycol = mydb.posts #Criando uma entidade/collections de nome posts

post1 = {
    "title": "Fast API",
    "category": "Back-End",
    "author": {
        "nome": "Paulo Bueno",
        "email:":"paulosilvabueno@hotmail.com"
    }
}

post2 = {
    "title": "Django",
    "category": "Back-End",
    "author": {
        "nome": "Paulo Bueno",
        "email:":"paulosilvabueno@hotmail.com"
    }
}

post3 = {
    "title": "N8N",
    "category": "Gestor de Automações",
    "author": {
        "nome": "Paulo Bueno",
        "email:":"paulosilvabueno@hotmail.com"
    }
}

result = mycol.insert_one(post1)
result2 = mycol.insert_many([post2, post3])
print("Documento inserido com sucesso!")
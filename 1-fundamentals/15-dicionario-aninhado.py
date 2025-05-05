import pprint

nameDicionary = {
    "Paulo Bueno":{
        "nomePais": [
            "Carlos Bueno",
            "Antonia Barros"
        ],
        "idade" : 33,
        "funcao" : "Desenvolvedor Full-Stack Java + React e Python + Django"
    },
    "Fabio Bueno" : {
        "nomePais": [
            "Carlos Bueno",
            "Antonia Barros"
        ],
        "idade" : 31,
        "funcao" : "Empresário"
    }
}

novoDicionario = {
    "Robério Bueno" : {
        "nomePais": [
            "Carlos Bueno",
            "Antonia Barros"
        ],
        "idade" : 37,
        "funcao" : "Técnico Eletricista"
    }

}

pp = pprint.PrettyPrinter(indent=10)
under = '-'

print(nameDicionary)
nameDicionary.update(novoDicionario)
pp.pprint(nameDicionary)

# 1 - Recuperar elementos do dicionario

print(f'{under *  50}\n')
# Forma 1
print(nameDicionary["Paulo Bueno"]["nomePais"])
# Forma 2
print(nameDicionary.get("Paulo Bueno"))

# 2 - Recuperar somente as chaves do dicionario
print(f'{under *  50}\n')
print(nameDicionary.keys())

# 3 - Recuperar apenas os valores do dicionario
print(f'{under *  50}\n')
print(nameDicionary.values())

# 4 - Retorna itens do dicionario com chave e valor como uma tupla
print(f'{under *  50}\n')
print(nameDicionary.items())

# 5 - Adicionar nova chave e valor no dicionario
print(f'{under *  50}\n')
nameDicionary["Carlos Bueno"] = {
    "nomePais": [
        "Francisco Bueno",
        "Etelvina Vieira"
    ],
    "idade" : 65,
    "funcao" : "Mestre de Obras"
}

nameDicionary["Fabio Bueno"]["funcao"] = "Chefe de Bar"
print(nameDicionary["Fabio Bueno"])
print(f'{under *  50}\n')
print(nameDicionary.get("Carlos Bueno"))

# 6 - Atualizar itens do dicionario
print(f'{under *  50}\n')
nameDicionary.update({"Paulo Bueno": {
    "funcao": "Cientista de Dados"
}})
print(nameDicionary)

# 7 - Deletando um dicionario
print(f'{under *  50}\n')
nameDicionary.pop("Carlos Bueno")
print(f'{under *  50}\n')
del nameDicionary["Paulo Bueno"]["funcao"]
print(nameDicionary)

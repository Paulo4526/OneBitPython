game = [
    {"nomeGame": "Age of Empires 2", "year":"1991", "interprise":"Ubsoft"},
    {"nomeGame": "Tibia", "year":"1998", "interprise":"Cipsoft"},
    {"nomeGame": "League of Legends", "year":"2010", "interprise":"Riot Games"},
    {"nomeGame": "Dracantos", "year":"2025", "interprise":"Unknow"},
    {"nomeGame": "PUBG", "year":"2016", "interprise":"Tecent"},
    {"nomeGame": "COD-Warzone", "year":"2022", "interprise":"Ubsoft"}
]

print(type(game))

gameSalvo = []

# 1 - Tamanho da lista
#Tamanho de itens dentro de 1 array
print(len(game))
#Tamanho de itens dentro de 1 objeto pelo indice
print(len(game[0]))
#Tamanho da string dentro de 1 atributo especifico em um objeto pelo indice
print(len(game[0]["nomeGame"]))

# 2 - Adicionando um objeto ao final do array
game.append({"nomeGame": "Need For Speed", "year":"2004", "interprise":"EA Sports"})
print(game)

# 3 - Ordenar lista
game.sort(key=lambda x: int(x["year"]))
print(game)

# 4 - Copiar itens de 1 lista para outra.
gameSalvo.append(game[0:3])
print(gameSalvo)

# 5 - Removendo 1 item de 1 lista
game.remove(game[0])
print(game)

# 6 - Removendo todos os itens da lista
gameSalvo.clear()
print(gameSalvo)

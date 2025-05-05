gamesTuplas = (
    {"nomeGame": "Age of Empires 2", "year":"1991", "interprise":"Ubsoft"},
    {"nomeGame": "Tibia", "year":"1998", "interprise":"Cipsoft"},
    {"nomeGame": "League of Legends", "year":"2010", "interprise":"Riot Games"},
    {"nomeGame": "Dracantos", "year":"2025", "interprise":"Unknow"},
    {"nomeGame": "PUBG", "year":"2016", "interprise":"Tecent"},
    {"nomeGame": "COD-Warzone", "year":"2022", "interprise":"Ubsoft"}
)

print(gamesTuplas)
print(type(gamesTuplas))

# Caracteristicas:
# - Não é possível adicionar valores dentro de 1 tupla
# - Não é possível remover valores dentro de 1 tupla
# - Não é possível ordenar valores na trupla.
# - Possibilita somente ser ordenads pelo metodo slice.

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuplas[0:2])

# 2 - Buscar o ultimo item da lista
print(gamesTuplas[-1])
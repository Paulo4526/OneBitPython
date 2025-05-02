game = [
    {"nomeGame": "Age of Empires 2", "year":"1991", "interprise":"Ubsoft"},
    {"nomeGame": "Tibia", "year":"1998", "interprise":"Cipsoft"},
    {"nomeGame": "League of Legends", "year":"2010", "interprise":"Riot Games"},
    {"nomeGame": "Dracantos", "year":"2025", "interprise":"Unknow"},
    {"nomeGame": "PUBG", "year":"2016", "interprise":"Tecent"},
    {"nomeGame": "COD-Warzone", "year":"2022", "interprise":"Ubsoft"}
]

#Aplicanto todos os conceitos aprendidos anteriormente com indices de listas(arrays) e dicionarios(objetos)
print(game[::2]) #Retorna o game a partir do primeiro indice e pulando de 2 em 2 após o primeiro indice.
print(game[0:3]) # Retorna jogos do primeiro ao terceiro indice
print(game[-1]) # Retorna o ultimo game
print(game[0]["nomeGame"].lower(), game[1]["nomeGame"][0:3]) #Retorna o nome em lowercase e o nome do game da string 0 até a 2
print(game[1]["year"].count("9"), game[0]["year"]) # Retorna o número de 9 dentro de year e retorna o valo de year.
print(game[1]["interprise"].upper(), game[0]["interprise"].split("o")) # Retorna o interprise maiusculo e empresa separado da letra "o"
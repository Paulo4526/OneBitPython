gameList = ["PUBG", "Tibia", "League of Legends", "CODE", "Age of Empires", "Tera Online"]

# 1 - Jeito normal de utilizar o form para uma lista
for i in range(len(gameList)):
    print(gameList[i])

# 2 - Utilizando o list comprehension
#Primeiramente estamos declarando a variavel "x", após isso a expressão "x in gameList" estamos atribuindo a "x" os itens de gameList
#Depois criamos a condicional caso haja o caractere "a" representado pelo operador "in" na lista x ele irá mostrar todos os jogos que contem o caractere "a"
newlist = [x for x in gameList if "a" in x]
print(newlist)

# 3 - Utilizando o list comprehension para mostrar os jogos diferente de "Tibia"
gameDiferent = [x for x in gameList if x != "Tibia"]
print(gameDiferent)


gameList = {"fifa", "pubg", "Red Dead 2", "Tibia", "COD"}

# 1 - Iterando valores de uma lista
for game in gameList:
    if len(game) < 5:
        print(f"O game {game} não corresponde as espeficiações necessárioas")
    else:
        print(f"O game {game} corresponde as especificações necessárias!")

# 2 - Quando a condição for atendida, o loop será encerrado
for game in gameList:
    if game == "Red Dead 2":
        break
    else:
        print(game)

# 3 - Quando a condição for atendida, o loop irá pular o valor e irá para a proxima iteração1!
for game in gameList:
    if game == "Red Dead 2":
        continue
    else:
        print(game)

# 4 - Avaliação do game
gameName = input("Digite o nome do jogo:\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no game:\n"))
sum = 0
for i in range(gameRating):
    note = float(input(f"Digite a {i + 1}º avaliação de {gameRating} para o game:\n"))
    sum += note
print(f"A média de avaliação do game {gameName} é de {sum/gameRating:.2f}")
gameName = input("Digite o nome do game:\n")
gameMenu = 0

while gameMenu != 3:
    gameMenu = int(input(
    """
    Menu:
    1 - Realizar Avaliações
    2 - Alterar o nome do game
    3 - sair
    """
    ))
    if gameMenu == 1:
        gameAvaliacao = int(input("Digite quantas avaliações deseja fazer:\n"))
        sum = 0
        for i in range(gameAvaliacao):
            note = float(input(f"Digite a {i + 1}º avaliação de {gameAvaliacao} para o game:\n"))
            sum += note
        print("Avaliação realizada com sucesso!")
        print(f"A média de avaliação do game {gameName} é de {sum/gameAvaliacao:.2f}")
    elif gameMenu == 2:
        newName = input("Digite o nome do game:\n")
        print(f"O nome do game {gameName} foi alterado com sucesso para {newName}!")
        gameName = newName
        continue

    else:
        print("Avalização finalizada com sucesso!")
        break
    confirm = int(input("""
    Deseja realizar mais avaliações?
    1 - sim
    2 - nao
    """))
    if confirm == 1:
        continue
    else:
        print("Avaliação finalizada com sucesso!")
        break
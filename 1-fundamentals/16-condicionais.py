# gameName = input("Digite o nome do jogo: \n")
# yearLaunch = int(input("Digite o ano de lançamento: \n"))
# classificacao = float(input("Digite a classificacao do jogo: \n"))

# if classificacao > 8.0:
#     print(f"A classificação {classificacao} do {gameName} siginifica que o game é exelente! Recomendado pela crítica!")
# elif classificacao < 8.0 and classificacao >= 5.0:
#     print(f"A classificação {classificacao} do {gameName} está abaixo da média! Pouco recomendado pela crítica!")
# else:
#     print(f"A classificação {classificacao} do {gameName} é muito ruim! Não é recomendado pela crítica!")
#
# if classificacao > 8.0 and yearLaunch > 2015:
#     print(f"O jogo {gameName} tem classificação {classificacao} e foi lançado em {yearLaunch}! Sendo um jogo novo e bom!")
# elif classificacao > 8.0 and yearLaunch < 2016:
#     print(f"A classificação {classificacao} do game {gameName} é exelente, porém, devido seu ano de lançamento ser em {yearLaunch}, não é tão jogado pelos novos jogadores!")
# elif classificacao < 8.0 and classificacao >= 5.0 and yearLaunch > 2015:
#     print(f"A classificação {classificacao} do game {gameName} é mediana,e devido seu ano de lançamento em {yearLaunch}, demonstra que há muito à melhorar!")
# elif classificacao < 8.0 and classificacao >= 5.0 and yearLaunch < 2016:
#     print(f"A classificação {classificacao} do game {gameName} é mediana, e devido seu ano de lançamento {yearLaunch}, não podemos esperar mais que isso devido a técnologia da época!")
# else:
#     print(f"O jogo {gameName} é ruim tendo uma classificação de {classificacao} e foi lançado em {yearLaunch}!")

print("Testando operadores!")
num1 = float(input("Digite o primeiro número da operação:\n"))
operator = input("Digite um dos operadores soma(+), subtração(-), divisão(/), multiplicação(*):\n")
num2 = float(input("Digite o segundo número da operação:\n"))

if operator == "+" or operator.lower() == "soma":
    print(f"{num1} + {num2} = {num1+num2:.0f}")
elif operator == "-" or operator.lower() == "subtração":
    print(f"{num1} - {num2} = {num1-num2:.0f}")
elif operator == "/" or operator.lower() == "divisão":
    print(f"{num1} / {num2} = {num1/num2:.0f}")
elif operator == "*" or operator.lower() == "multiplicação":
    print(f"{num1} * {num2} = {num1*num2:.0f}")
else:
    print("Operador inválido! Tente novamente com o operador correto!")
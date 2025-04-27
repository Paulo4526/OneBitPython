#Ultilizando inputs
''''
Comentário em multiplas linhas
'''

name = input('Digite o nome do jogo:\n')
yearLaunch = int(input('Digite o ano de lançamento:\n'))
premiumPrice = float(input('Digite o valor do premium:\n'))
planFull = bool(input('É um plano full?\n'))

print(f'Nome do Game: {name}\nAno de Lançamento: {yearLaunch}\nPreço do Premium: {premiumPrice}\nPlano completo: {planFull}')
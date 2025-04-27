gameDescription = ''''
    Fifa 2023 é um jogo de futebol desenvolvido pela EA Sports
    e que possibilita jogar localmente ou online.
'''

#Conferindo se existe um determinado valor em game descriptions podendo ser leta números palavras espaços e etc.
print("!" in gameDescription)

fifaName = 'Fifa'
fifaVersion = '23'
#Operacáo de contatenação
fifaFullName = fifaName + ' ' + fifaVersion
print(fifaFullName)

#Operaçao de multiplicação com string
evilName = 'Residente Evil'
evilVertsion = '3.0v'
multString = len(evilName) * len(evilVertsion)
print(multString)

#Operaçao de multiplicaçao para aumentar a quantidade de strings
line = '='
asterisco = '*'
print((line * len(evilName) + (asterisco * len(evilVertsion))))

#Exemplo prático abaixo irá mostrar exatamente o mesmo tamanho de strind com o underScore
title = 'Praticando python com multiplicaçao utilizando strings'
under = '-'
print(f'{under * len(title)}\n{title}\n{under * len(title)}')
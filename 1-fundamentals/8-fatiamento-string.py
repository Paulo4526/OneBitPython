nome = 'PaulodaSilvaBueno'

#Buscar string a partir da primeira posição
print(nome[0:])

#Busca da primeira posição até a sexta posição.
print(nome[0:5])

#Busco o indice desde a segunda posição até a decima primeira, e só mostrarei o indice que está pulando de 3 em 3 casas ou seja o indice 1 4 7 e 10
print(nome[0:10:3])

#Buscando o indice iniciando da ultima posição até a primeira
print(nome[10:0:-1])

#OBS: Lembrando que quando vazio "[::1]" ele pega do primeiro ao ultimo indice de forma automatica, quando invertemos como [::-1] o indice do meio é o inicial e o primeiro o final
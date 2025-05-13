import statistics
media = [1,3,5,8,9]
mediana = [2,3,4,5,6]
moda = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,1,1,1,3,3,3,4,5,]
desvio = [1, 0.5, 1.2, 2.3, 2.5, 3.5, 1.0]
# 1 - Aplicar a média
print(statistics.mean(media)) #Informando uma varável para a média
print(statistics.mean([1,4,8,10,5,7,8])) #Atribuindo valores de forma manual à média

# 2 - Aplicar a mediana
print(statistics.median(mediana)) #Informando uma variavel para a mediana
print(statistics.median([4,8,10,5,7,8])) #Atribuindo valores de forma manual à mediana

# 3 - Aplicar a moda(Mostra o número que mais se repete)
print(statistics.mode(moda))

# 4 - Desvio padrão(Utilizando análise exploratória)
"""
Quanto mais próximo de 0 for o desvio padrão, 
significa que os dados do conjunto estão menos dispersos
"""
print(statistics.stdev(desvio))
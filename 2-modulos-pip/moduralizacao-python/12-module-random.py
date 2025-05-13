import random

# 1 - Seleciona um valor aleatório de uma lista
list = [10,13,12,13,112,13,14,15,16,112,11,233]
print(random.choice(list))

# 2 - Gerando um número aleatório em intervalo de valores
r1 = random.randint(0, 15)
print(r1)

# 3 - Seleciona um caractere aleatório de uma string
name = "Curso de desenvolvedor Java"
r2 = random.choice(name)
print(r2)

# 4 - Selecione mais de 1 valor aleatório
#Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(name,10))
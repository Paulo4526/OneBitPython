from collections import Counter, namedtuple, deque
from operator import itemgetter

lista = ["Maçã", "Banana", "Laranja", "Melancia", "Melão", "Pitaya", "Abacaxi", "Uva", "Banana", "Laranja" , "Melão", "Pitaya", "Abacaxi"]

# 1 - Agrupa e conta itens de uma lista
print(lista)
print(Counter(lista))

# 2 - Utilizando tupla nomeada
#Criando uma variavél que recebe valores
game = namedtuple('game', ['name', 'note', 'yearLaunch'])
g1 = game("Fifa23", 5.0, 2023)
g2 = game('PUBG', 4.9, 2017)
print(f"Game 1: {g1}, Game 2: {g2}")

# 3 - Ordenando dicionario
studants = {"Paulo": 33, "Ana": 23, "Fabio": 32, "Carlos": 65, "Antonia": 63}
a = sorted(studants.items(), key=itemgetter(0))
print(a)

# 4 - Utilziando fila de ambas a extemidades
deq = deque([20, 40, 60, 80])
deq.append(10)
print(deq)
deq.append(90)
print(deq)
deq.popleft()
print(deq)
deq.pop()
print(deq)
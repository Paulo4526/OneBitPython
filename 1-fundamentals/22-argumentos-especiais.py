"""
*args - utilizamos quando não temos certeza de quantos argumentos temos numa função e são passados como tuplas.
**kwargs - Além dos valores, podemos passar também as respectivas chaves passados como um dicionario ou data-set.
"""

# 1 - Soma de números com *args
def sum(*num):
    sum_total = 0
    for i in num:
        sum_total += i
    print(f"A soma é: {sum_total}")

sum(7, 9, 10, 11,24,50)

# 2- Apresentando valors com **kwargs
def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

participantes = {"Nome": "Paulo", "idade": 33, "cidade": "Itaquaquecetuba", "estado": "São Paulo"}
presentation(**participantes)
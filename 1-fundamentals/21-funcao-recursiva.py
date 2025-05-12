# 1 - Fatorial de multiplicação de 1 número:
"""
Fatorial de um número:
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""

def factorial1(num):
    if num == 1:
        return 1
    else:
        return num * factorial1(num-1)
print(f"O valor factorial é de {factorial1(7)}")

#2 - Soma total de um número factorial
"""
5 -> 5 + 4 + 3 + 2 + 1
4 -> 4 + 3 + 2 + 1
"""
def factorial2(num):
    if num == 1:
        return 1
    else:
        return num + factorial2(num-1)
print(f"O valor total da soma é de {factorial2(5)}")
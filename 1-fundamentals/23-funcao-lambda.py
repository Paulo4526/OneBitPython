# 1- Função de potência de número
power = lambda num: num ** 2

# 2 - Função que verifica se o número é par caso o resto da divisão seja 0
pair = lambda x: x % 2 == 0

# 3 - Função que divide umm numero por outro
divNum = lambda x,y : x / y

# 4 - Funçãoq ue inverte uma string
reverse = lambda s: s[::-1]

print(f"O valor da potência de 5 é {power(5)}")
print(f"O número 11 é par? {pair(11)}")
print(f"O valor da divisão entre 10 e 2 é {divNum(10,2):.1f}")
print(f"A inversão de string de JavaScript é {reverse("JavaScript")}")

import math

# 1 - Acessando número Pi
print(math.pi)
print(f"Formatando Pi {math.pi:.2f}")

# 2 - Acessar o número de Euler
print(math.e)
print(f"Formatando Euler {math.e:.2f}")

# 3 - Arredondando número para cima
num1 = 10.54
print(math.ceil(num1))

# 4 - Arredondando número apra baixo
print(math.floor(num1))

# 5 - Fatorial de um número
num2 = int(input("Digite um numero factorial:\n"))
print(math.factorial(num2))

# 6 - Potência de números sendo 2 elevado a décima
print(math.pow(2,10))

# 7 - Raiz quadrada de um número
print(f"Raiz quadrada de 179 é {math.sqrt(178):.2f}")

# 8 - Máximo divisor comum(MDC)
mdc = math.gcd(25,120) # resultado é qual o maior divisor comum entre os 2 números
print(mdc)

# 9 - Logaritimo
print(math.log(10))

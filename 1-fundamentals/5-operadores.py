#Operadores

num1 = int(input('Digite o primeiro número da operação:\n'))
num2 = int(input('Digite o segund número da operação\n'))

# Operadores Aritiméticos
print('Operadores Aritiméticos')
#Soma '+'
soma = num1 + num2
print(f'A soma entre {num1} e {num2} é = {soma}')

#Subtração '-'
subtracao = num1 - num2
print(f'A subtraçao entre {num1} e {num2} é = {subtracao}')

#Divisão '/'
divisao = num1 / num2
print(f'A divisão entre {num1} e {num2} é = {divisao}')

#Multiplicação '*'
multiplicacao = num1 * num2
print(f'A Multiplicação entre {num1} e {num2} é = {multiplicacao}')

#Resto da Operação '%'
resto = num1 % num2
print(f'O resto da operação é {resto}')

#Exponenciação '**'
expo = num1 ** num2
print(f'O valor {num1} elevado a {num2} é = {expo}')

#Operador de Comparaçào
print('\nOperadores de Compraração\n')
#Maior que '>'
maiorQue = num1 > num2
print(f'{num1} é maior que {num2}? {maiorQue}')

#Menor que '<'
menorQue = num1 < num2
print(f'{num1} é menor que {num2}? {menorQue}')

#Maior ou igual '>='
maiorIgual = num1 >= num2
print(f'{num1} é maior ou igual a {num2}? {maiorIgual}')

#Menor ou igual '<='
menorIgual = num1 <= num2
print(f'{num1} é menor ou igual a {num2}? {menorIgual}')

#Diferente de '!='
diferente = num1 != num2
print(f'{num1} diferente de {num2}? {diferente}')

#Exatamente igual '=='
exatamenteIgual = num1 == num2
print(f'{num1} é exatamente igual a {num2}? {exatamenteIgual}')

#Comparando Tipos
tipoIgual = type(divisao) == type(subtracao)
print(f'{type(divisao)} é igual a {type(subtracao)} = {tipoIgual}')

tipoIgual2 = type(soma) == type(subtracao)
print(f'{type(soma)} é igual a {type(subtracao)} = {tipoIgual2}')



#Criando a função simples
def novaFuncao():
    print("Hello World!")

novaFuncao()

#Função que recebe parametros
def sum(num1, num2):
    return num1 + num2

newValue = sum(4, 5)
print(f"Valor da função sum é: {sum(4,5)}")
print(newValue)

#Função que recebe valor por default caso não seja passado nenhum outro valor
def country(pais="Brasil"):
    return pais.upper()
#Aqui como informado, estamos utilizando um valor default, caso não passarmos nada ele irá informar o valor default
print(f"Eu moro no país chamado {country()}")
#Como vemos abaixo caso passarmos um valor ele substituirá o valor pré-definido
print(f"Eu moro no país chamado {country("Australia")}")
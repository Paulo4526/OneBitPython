#Expressão regular em python
import re

text = "OnBitCode: Transformamos pressoas em programadores sem limites"
site = 'https://onebitcode.com'
frase = 'Estudando python para construção de dashboards e integração com front-end react + java'
frase2 =["Olá amigos, vamos estudar python?", "Não, hoje estudaremos java com spring boot!"]
# 1 - Índice inicial e final de palavras
# O r significa que estamos trabalhando com a string bruta(raw string)
match = re.search(r'programadores', text) #Dentro de parenteses após declarar "r" dentro de aspas informamos qual palavra ou texto queremos buscar, e após a virgula informamos o texto bruto ou uma variavel.
print(f"Indice inicial {match.start()}")
print(f"Indice final {match.end()}")

# 2 - Buscando o índice que possui o ponto
match2 = re.search(r'://onebitcode', site) #Para buscar valores dentro de um site
match3 = re.search(r'\.', site) #Para buscar um ponto final exatamente utilizar a contra barra
print(f"O valor da busca foi de: {match2}")
print(f"O valor da busca foi de: {match3}")

# 3 - Buscando uma lista de caracteres dentro de uma frase
#O padrão seta somente que será procurado as letras de forma separada de a-f
padrao = "[a-f]"
#Aqui informamos qual a variavel padrão de busca dentro da frase, e ele buscara dentro de cada palavra somente as letras da busca
result = re.findall(padrao, frase)
print(f"Frase completa: {frase}")
print(f"Frase onde procuramos somente os caracteres de forma separada de a à f {result}")

# 4 - Verificando o início de uma string
rule = r'^O' #Regra para verificar quando a frase começa com a letra A maiuscula em 1 array, caso seja um objeto ele fará com o próprio index e criará uma resposta enorme
for f in frase2:
    if re.search(rule, f):
        print(f"O valor corresponde à busca: {f}")
    else:
        print(f"O valor não corresponde à busca: {f}")


# 5 - Verifica o final da string
rule_end = r'!$' #Aqui verificamos se a frase termina com exclamação informando "!" e o cifrão no final "$" para verificar se termina com.
match4 = re.search(rule_end, frase)
if match4:
    print(f"A frase finaliza com o ponto de esclamação!")
else:
    print(f"A frase não finaliza com o ponto de exclamação")
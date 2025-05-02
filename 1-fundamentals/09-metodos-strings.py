nome = "Paulo da Silva Bueno"
informacoes = """
adicionando informações aleatorias para treinar manipulação de strings
abaixo iniciaremos os metodos de manipulação de strins em python
"""

print(nome.upper()) # Retorna a string maiuscula
print(nome.lower()) # Retorna a string minuscula
print(nome.capitalize()) # Retorna a string com apenas a primeira lentra em maiusculo todas as outras serão minusculas
print(nome.title()) # Retorna a string com apenas a primeira letra em maiusculo todas as outras serão minusculas
print(nome.center(50, '-')) # Informa que o mínimo de string deverá ser 50, caso não chegue a 50 será preenchido com "-", caso ultrapasse não será adicionado strings
print(nome.find("u")) #Retorna a posição da primeira string especificada, no nosso caso "a".
print(informacoes.count("i")) #Contará quantos caracteres tem dentro de uma variável string
print(informacoes.replace("i", "HELLO")) #Altera o valor de uma string para outra. Ou seja todas as letras i do texto se tornarão HELLO.
print(informacoes.split(" ")) #Quebra a linha onde terá o caracter especificado que no nosso caso é espaço porém, pode ser uma letra em especifico e etc.
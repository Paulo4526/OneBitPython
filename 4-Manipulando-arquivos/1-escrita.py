name = input("Digite o seu nome:\n")
#Salvando o valor da variavel em 1 arquivo
#Aqui criamos uma variavel com uma função open, e dentro de open teremos 3 opções:
#'r' = Para read de leitura
#'w' = Para write de escrita
#'a' = Para append caso deseja incluir ou adicionar alguma palavra
#Primeiramente dentro de open, escrevemos o nome do arquivo e o modo que queremos que no nosso caso será write devido ser um novo arquivo.
#Criando arquivo/sobreescrevendo arquivo
file1 = open('arquivos/names.txt', 'w')
file1.write(name)
file1.close()

#Adicionando itens ao arquivo
#Alternativa 1
# option = ""
# while option.lower() == 'sim' or option == "" or option.lower() == 's':
#     newOption = input("Deseja adicionar outro nome?\n")
#     option = newOption
#     if option.lower() == "sim" or option.lower() == "s":
#         newName = input("Digite o seu nome completo:\n")
#         name = newName
#         #Adicionando...
#         file2 = open('arquivos/names.txt', 'a')
#         file2.write(f"\n{name}")
#         file2.close()
#     else:
#         break

#Alternativa 2 com o with ao invés de iniciar uma varoavel
option = ""
while option.lower() == 'sim' or option == "" or option.lower() == 's':
    newOption = input("Deseja adicionar outro nome?\n")
    option = newOption
    if option.lower() == "sim" or option.lower() == "s":
        newName = input("Digite o seu nome completo:\n")
        name = newName
        #Adicionando...
        with open('arquivos/names.txt', 'a') as file2:
            file2.write(f"\n{name}")
    else:
        break

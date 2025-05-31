#Aqui trabalharemos a escrita junto à leitura para praticarmos
#Daqui para frente utilizaremos a opção com o with ao invés de criarmos uma variável.
content = input("Digite o conteúdo do arquivo:\n")
with open("arquivos/criando-arquivo.txt", 'w') as arquivo:
    arquivo.write(content.upper())

option = ""
while option != "3" or option.lower() == "sair":
    option = input(f"Selecione uma opção: \n1-Adicionar Conteúdo ao arquivo \n2-Ler o conteúdo do arquivo \n3-Sair\n")
    if option.lower() == "adicionar" or option == "1":
        content = input("Digite o conteúdo a ser adicionar:\n")
        with open("arquivos/criando-arquivo.txt", 'a') as adicionar:
            adicionar.write(f"\n{content.upper()}")
    elif option.lower() == "ler" or option == "2":
        with open("arquivos/criando-arquivo.txt", 'r', encoding='utf-8') as arquivo:
            for line in arquivo:
                print(line.rstrip())
    elif option.lower() == "3" or option.lower() == "sair":
        break
    else:
        print("Opção inválida!")
        continue
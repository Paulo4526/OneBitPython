import sqlite3 as lite

#1 - Conectando ao banco de dados
connection = lite.connect('title.db')

#2 - Criando o cursor
cursor = connection.cursor()

#3 - Alterando os dados
option = ''

while option != 0:
    id_filme = int(input("Qual o id do filme que deseja alterar:\n"))
    # recuperando dados do filme
    for row in cursor.execute('select * from filmes where id == ?;', (id_filme,)):
        print(f"Dados do filme\n{row}")
    confirm = int(input('''
        \nDeseja alterar o filme?
        \n1 - Sim
        \n2 - Não
    '''))
    if confirm == 1:
        filme_select = int(input('''
            \nO que deseja alterar no filme?
            \n1 - Nome do filme
            \n2 - Genero do filme
            \n3 - Ano do filme
            \n4 - Todos os dados
            \n0 - Cancelar e Sair
        '''))
        if filme_select == 1:
            nome_filme = input("Digite o novo nome do filme:\n")
            cursor.execute('''
                update filmes set nome_filme == ? where id == ?;
            ''', (nome_filme, id_filme))
            connection.commit()
            print("Filme alterado com sucesso!")
            break

        elif filme_select == 2:
            genero_filme = input("Digite o novo genero do filme:\n")
            cursor.execute('''
                update filmes set genero_filme == ? where id == ?;
            ''', (genero_filme, id_filme))
            connection.commit()
            print("Filme alterado com sucesso!")
            break

        elif filme_select == 3:
            ano_lancamento = int(input("Digite o novo ano de lançamento do filme:\n"))
            cursor.execute('''
                    update filmes set ano_lancamento == ? where id == ?;
                ''', (ano_lancamento, id_filme))
            connection.commit()
            print("Filme alterado com sucesso!")
            break

        elif filme_select == 4:
            nome_filme = input("Digite o novo nome do filme:\n")
            genero_filme = input("Digite o novo genero do filme:\n")
            ano_lancamento = int(input("Digite o novo ano de lançamento do filme:\n"))
            cursor.execute('''
                update filmes set nome_filme == ?, genero_filme == ?, ano_lancamento == ? where id == ?;
            ''', (nome_filme, genero_filme, ano_lancamento, id_filme))
            connection.commit()
            print("Filme alterado com sucesso!")
            break

        elif filme_select == 0:
            option = 0
            print("Operação cancelada com sucesso!")
    elif confirm == 2:
        option = 0
        print("Operação cancelada com sucesso!")

connection.close()


import  sqlite3 as lite

#1 - Conectando ao banco de dados
connection = lite.connect('title.db')

#2 - Criando o cursor
cursor = connection.cursor()

#3 - Deletando dados
id_filme = int(input('Digite o id do filme que deseja deletar?\n'))
exist = 0
for row in cursor.execute('select * from filmes where id == ?;', (id_filme,)):
    if row == '':
        break
    else:
        print(f"Dados do filme:\n{row}")
        exist = 1

if exist == 1:
    deletar = input('''
    Deseja realmente deletar o filme:
    1 - Sim
    2 - Não
    ''')

    if deletar.upper() == 'SIM' or int(deletar) == 1:
        cursor.execute('delete from filmes where id == ?;', (id_filme,))
        connection.commit()
        print('Filme deletado com sucesso!')
        connection.close()
    elif deletar.upper() == 'NÃO' or int(deletar) == 2:
        print("Operação cancelada!")
        connection.close()
else:
    print("Filme não encontrado ou não existe, por favor reinicie a aplicação e digite um id valido!")
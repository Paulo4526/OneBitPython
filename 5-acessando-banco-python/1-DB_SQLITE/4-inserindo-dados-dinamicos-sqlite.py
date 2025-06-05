import sqlite3 as lite

#1 - Conectando com o banco de dados
connection = lite.connect('title.db')

#2 - Criando o cursor
cursor = connection.cursor()

# Solicitando dados do usuário
nome = input('Digite o nome do filme:\n')
genero = input('Digite o genero do filme:\n')
ano_lancamento = int(input('Digite o ano de lancamento:\n'))

#4 - Inserindo dados de forma dinamica através de uma variavel
cursor.execute('''
    insert into filmes(nome_filme, genero_filme, ano_lancamento)
    values(?,?,?);
''', (nome, genero, ano_lancamento))
# É passado após o comando em forma de tupla os valores de cada parametro na sua ordem
#em java é parecido o comando.

#5 - Salvando as alterações no banco de dados
connection.commit()
print('Dados salvos com sucesso no banco de dados!')

#6 - Fechando a conexão com o banco de dados
connection.close()
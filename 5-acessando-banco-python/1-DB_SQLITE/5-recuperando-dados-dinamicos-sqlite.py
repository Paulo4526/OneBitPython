import sqlite3 as lite

# 1 - Conectando com o banco de dados
connection = lite.connect('title.db')

# 2 - Criando o cursor
cursor = connection.cursor()

# 3 - Lendo dados a partir de uma tabela
nome_filme = input('Digite o nome do filme que quer consultar:\n')
cursor.execute('''select * from filmes where nome_filme == ?''', (nome_filme,))
print(cursor.fetchall())

# 4 - Interando os dados
for row in cursor.execute('select * from filmes'):
    print(f"{row}")

# 4 - Fechando a conexão
print('Fechando conexão')
connection.close()

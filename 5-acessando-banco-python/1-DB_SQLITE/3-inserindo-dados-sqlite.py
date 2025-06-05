import sqlite3 as lite

#1 - Conectando novamente ao banco de dados
connection = lite.connect('title.db')

#2 - Utilizando o cursor
cursor = connection.cursor()

# 3 - Inserindo dados no banco de dados
cursor.execute('''
    insert into filmes (nome_filme, genero_filme, ano_lancamento) values ('Jurassic Park 3', 'Ação e Suspense', 2003);
''')

#4 - Confirmando as alterações no banco de dados
connection.commit()
print('Dados Salvos com sucesso!')

#5 - Fechando a conexão
connection.close()


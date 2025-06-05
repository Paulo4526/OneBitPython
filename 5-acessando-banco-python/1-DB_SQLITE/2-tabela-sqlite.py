import sqlite3 as lite

#1 - Conectando com o banco de dados criado no passo 1
connection = lite.connect('title.db')

#2 - Criando um cursor para manipular o DML(Manipular os dados) ou DDL(Estrutura de dados)
#Estanciando o cursor
cursor = connection.cursor()

#3 - Criando a tabela
cursor.execute('''
    create table filmes(
        id integer not null primary key AUTOINCREMENT,
        nome_filme varchar(100) not null,
        genero_filme varchar(100) not null,
        ano_lancamento integer not null
    );
''')

#4 - Fechando a conexão
print(f"Tabela criada com sucesso!")
connection.close()


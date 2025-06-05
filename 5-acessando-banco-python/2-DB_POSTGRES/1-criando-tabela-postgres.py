from conexão_py import connect

#1 - Criando o cursor
cursor_obj = connect.cursor()
print(cursor_obj)#para verificar se a conexão foi efetuada, caso haja 1 erro de conexão.

#2 - criando uma tabela
cursor_obj.execute('''
    create table funcionario(
        id serial primary key,
        nome varchar(100) not null,
        funcao varchar(100) not null,
        idade integer not null
    );
''')
connect.commit()
connect.close()
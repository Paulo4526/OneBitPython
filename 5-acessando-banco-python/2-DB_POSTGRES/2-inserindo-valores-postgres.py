from conexão_py import connect

#1 - Criando cursor
cursor = connect.cursor()

funcionario = [
    ('Paulo Bueno', 'Eletricista', 33),
    ('Carlos Bueno', 'Pedreiro', 65),
    ('Fabio Bueno', 'Barman', 31),
    ('Anotnia Barros', 'Aposentada', 63)
]

#2 - Inserindo valores na tabela passando parametros
for func in funcionario:
    cursor.execute('''
        insert into funcionario(nome, funcao, idade) values(%s, %s, %s)
    ''', func)
    connect.commit()
connect.close()
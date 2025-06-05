from conexão_py import connect

#1 - Criando o cursor
cursor = connect.cursor()

#2 - Alterando dados
cursor.execute('update funcionario set nome= %s where id = 2', ('Clelia Bueno',))
connect.commit()
connect.close()
from conexão_py import connect

#1 - Criando cursor
cursor = connect.cursor()

#2 - excluindo um dado da tabela ou dados
cursor.execute("delete from funcionario where id = 1")
connect.commit()
print('Dados excluidos com sucesso!')
connect.close()
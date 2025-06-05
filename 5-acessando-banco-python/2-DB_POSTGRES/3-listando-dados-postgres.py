from conexão_py import connect

#1 - Criando o cursor
cursor = connect.cursor()

#2 - Listando valores
cursor.execute("select * from funcionario order by idade desc")
result = cursor.fetchall()
#Diferente do SQLite não conseguimos fazer uma iteração direta, sendo assim precisamos do resultado do fetchall antes de interar
for row in result:
    print(f"Funcionario {row[1]}:\nDados: id({row[0]}), Função({row[2]}), Idade({row[3]})\n")
connect.close()
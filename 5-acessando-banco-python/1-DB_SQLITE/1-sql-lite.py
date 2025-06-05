import sqlite3 as lite

#1 - Criando o banco de dados, esta é uma forma convencional, caso o banco de dados já esteja criado
#ele se conecta de forma automática, caso não exista ele cria e se conecta ao banco mencionado.
connection = lite.connect("title.db")

# 2 - Verifica se houve alterações na base de dados
print(connection.total_changes)

nameSet = {"Paulo Bueno", "Carlos Bueno", "Antonia Barros", "Etelvina Vieira", "Fabio Bueno", "Roberio Bueno"}
exempleSet = {"FIAP", "Alura", "DIO", "OneBitCode"}

# 1 - Buscar tamanho do set
print(len(nameSet))
print(nameSet)

# 2 - Adicionando itens de 1 set a outro set.
nameSet.update(exempleSet)
print(nameSet)

# 3 - Remover itens do set
nameSet.remove("FIAP")
print(nameSet)

# Não permite valores duplicados no set.
# Não permite recuperar valores via fatiamento ou slice
nameDicionary = {
    "nome": "Paulo Bueno",
    "nomePais": [
        "Carlos Bueno",
        "Antonia Barros"
    ],
    "idade" : 33,
    "funcao" : "Desenvolvedor Full-Stack Java + React e Python + Django"
}

print(nameDicionary)
print(nameDicionary["nomePais"])
print(len(nameDicionary))
print(type(nameDicionary))

# 1 - Recuperar elementos do dicionario
# Forma 1
print(nameDicionary["nome"])
# Forma 2
print(nameDicionary.get("idade"))

# 2 - Recuperar somente as chaves do dicionario
print(nameDicionary.keys())

# 3 - Recuperar apenas os valores do dicionario
print(nameDicionary.values())

# 4 - Retorna itens do dicionario com chave e valor como uma tupla
print(nameDicionary.items())

# 5 - Adicionar nova chave e valor no dicionario
nameDicionary["estado"] = "sp"
nameDicionary["cidade"] = "Itaquaquecetuba"
print(nameDicionary)

# 6 - Atualizar itens do dicionario
nameDicionary.update({"estado": "São Paulo"})
print(nameDicionary)

# 7 - Remover itens do dicionario
nameDicionary.pop("funcao")
print(nameDicionary)
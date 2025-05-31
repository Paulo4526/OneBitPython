names = []

with open("arquivos/names.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        names.append(linha.strip()) #Strip para remover os espaços

#Ordenadar de forma ordenada e revsersa
print(f"\nOrdenando nome de forma reversa ou decrescente:\n")
for nome in sorted(names, reverse=True):
    print(nome)

print(f"\nOrdenando nome de forma crescente:\n")
#Ordenar de forma ordenada
for name in sorted(names):
    print(name)
import csv

courses = [
    {"Java" : "Spring Boot"},
    {"Python" : "Django"},
    {"NodeJS" : "Prisma"},
    {"ReactJS" : "TypeScript"},
    {"NextJS": "TypeScript"}
]
#Criando manualmente o arquivo csv
with open("arquivos/courses.csv", "w") as arquivo:
    for course in courses:
        for chave, valor in course.items(): #aplicando conceito de desestruturação em python com chave e valor
            arquivo.write(f"{chave}, {valor}\n")

#Lendo o arquivo CSV
with open("arquivos/courses.csv", "r", encoding="utf-8") as arquivo:
    #Mostrando os valores formatados(descomente abaixo para ver o funcionamento)
    # for chave, valor in csv.reader(arquivo):
    #     print(f"Curso: {chave}, Tecnologia de Apoio: {valor}")

    for line in arquivo:
        row = line.rstrip().split(",") #Transformando o item em um array com split
        lenguage, tecnology = line.rstrip().split(",") #Aplicando conceito de desestruturação em python usando array
        print(f"Antes da formatação: {row}")
        print(f"Depois da formatação: \nLinguagem: {lenguage} \nTecnologia: {tecnology}\n")

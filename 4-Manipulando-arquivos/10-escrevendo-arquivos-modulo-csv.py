import csv
courses = []

course = input("Qual a linguagem que gostaria de aprender?\n")
tecnology = input(f"Qual a biblioteca que gostaria de aprender junto ao {course}\n")

with open("arquivos/courses.csv", "a", encoding="utf-8") as arquivo:
    write = csv.writer(arquivo, lineterminator='\n')
    write.writerow([course, tecnology])
    print("Arquivo atualizado com sucesso!")

with open("arquivos/courses.csv", "r", encoding="utf-8") as arquivo:
    read = csv.DictReader(arquivo)
    for row in read:
        courses.append({"language": row["language"], "tecnology": row["tecnology"]})

for course in sorted(courses, key=lambda x: x["language"]):
    print(f"{course['language']} - {course['tecnology']}")

courses = []
#Recebendo os dados e transformando em dicionarios e salvando em courses
with open("arquivos/courses.csv", "r") as arquivo:
    for line in arquivo:
        language, tecnology = line.strip().split(",")
        course = {}
        course["language"] = language
        course["tecnology"] = tecnology
        courses.append(course)
print(courses)

for course in courses:
    print("Recebendo somente os valores de cada chave do array")
    print(f"{course['language']}, {course['tecnology']}")
    # for chave, valor in course.items():
    #     print("Recebendo a chave e o valor de cada array")
    #     print(f"{chave}: {valor}\n")
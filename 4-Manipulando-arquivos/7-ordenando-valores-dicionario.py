courses = []

with open("arquivos/courses.csv", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lenguage, tecnology = linha.rstrip().split(",")
        course = {}
        course["language"] = lenguage
        course["tecnology"] = tecnology
        courses.append(course)
print(courses)

#Função que recebe uma chave e retorna o valor da chave para language
def get_language(course):
    return course["language"]

#Função que recebe uma chave e retorna o valor da chave para tecnology
def get_tecnology(course):
    return course["tecnology"]

#Para usar o sorted com chaves é preciso criar uma função para pesquisar os valores de cada chave e agrupar de acordo.
#Aqui optamos por ordenar de acordo com o valor da chave language, mas também poderia ordenar de acordo com a chave tecnology
for course in sorted(courses, key=get_language):
    print(f"{course['language']} - {course['tecnology']}")
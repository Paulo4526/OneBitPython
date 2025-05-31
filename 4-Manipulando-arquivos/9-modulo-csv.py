import csv

courses = []

with open("arquivos/courses.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.DictReader(arquivo)
    for row in reader:
        courses.append({"language":row["language"],"tecnology":row["tecnology"]})

for course in sorted(courses, key=lambda k: k['tecnology']):
    print(f"{course['language']} - {course['tecnology']}")
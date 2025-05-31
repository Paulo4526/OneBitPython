courses = []

with open("arquivos/courses.csv", "r", encoding="utf-8") as arquivo:
    for line in arquivo:
        language, tecnology = line.rstrip().split(",")
        course ={}
        course["language"] = language
        course["tecnology"] = tecnology
        courses.append(course)

print(courses)

for course in sorted(courses, key=lambda x: x["tecnology"]):
    print(f"{course['language']}, {course['tecnology']}")

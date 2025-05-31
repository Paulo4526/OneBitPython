courses = []

with open("arquivos/courses.csv", "r", encoding="utf-8") as arquivo:
    for line in arquivo:
        language, tecnology = line.rstrip().split(',')
        courses.append(f"{language},{tecnology}")
        
print(courses)
for course in sorted(courses):
    print(course)
import json

# 1 - Converter string para dicionario
person = '{"name": "Paulo Bueno", "languages": ["Python", "Java", "NodeJS"]}'
person_dict = json.loads(person)
print(person_dict)
print(type(person_dict))
print(person_dict['languages'])

# 2 -  Convertendo dicionario para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))

# 3 - Formatando o json
print(json.dumps(person_dict, indent=4, sort_keys=True)) #Aplicando indentação

# 4 - Salvando o json em txt no nosso diretório
with open('person.txt', 'w') as json_file: #Aqui usamos a letra "w" de write
    json.dump(person_dict, json_file)

# 5 - Lendo um arquvivo no formato json
with open('user.json', 'r') as f: #Aqui usamos a letra "r" de read para leitura
    data = json.load(f)
    print(json.dumps(data, indent=4, sort_keys=True))
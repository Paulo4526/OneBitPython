#Desafio para pegar a média da soma de notas e Antecessdor e sucessor da média
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
nota5 = int(input("Digite a quinta nota: "))

notas = [nota1, nota2, nota3,nota4,nota5]
soma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4]
media = soma / len(notas)
print(media)
print(f'O Sucessor da média {media} é {media + 1}\nO Antecessor da média {media} é {media - 1 }')



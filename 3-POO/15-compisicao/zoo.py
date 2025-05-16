class Zoo:
    def __init__(self):#Criando um construtor que recebe um objeto dicionario podendo ser vazio
        self.animals_dict = {}

    def add_animal(self, animal): #Criando metodo que recebe um objeto e armazena no nosso construtor
        self.animals_dict[animal.name] = animal  # Armazena o objeto

    def total_of_category(self, category): #Verificação do objeto com o valor de uma categoria como parametro
        result = 0
        for animal in self.animals_dict.values(): #Atribui o valor do objeto à variavel animal
            if animal.category == category: #Faz a comparação caso a categoria do ainmal seja a passada como parametro realiza a contagem e printa.
                result += 1
        return f"No nosso zoológico temos {result} animais da categoria {category}"

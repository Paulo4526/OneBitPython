class Funcionario:
    empresa = "CCR"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"\nNome: {self.nome}, \nIdade: {self.idade}, \nEmpresa: {self.empresa}\n"

    def func_info(self):
        print(f"Funcionario: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nome da empresa: {self.empresa}\n")

Funcionario.empresa = "Motiva" #Metodo que altera a variavel/atributo de uma classe
paulo = Funcionario("Paulo", 33)
paulo.func_info()
print(paulo)

Funcionario.empresa = "Autonomo" #Metodo que altera a variavel/atributo de uma classe
carlos = Funcionario("Carlos", 65)
carlos.func_info()
print(carlos)

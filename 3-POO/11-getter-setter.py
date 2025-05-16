class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary #"__" modifica o atributo para private

    def show_details(self):
        print(f"\nNome: {self.name} \nSalary: {self.__salary}\n")

    #Metodo get para pegar o valor de atributos privado
    def get_salary(self):
        return self.__salary

    #Metodo set atribuir ou alterar o valor de atributos privado
    def set_salary(self, salary):
        self.__salary = salary

fulano = Employee("Fulano", 5000)
ciclano = Employee("Ciclano", 5000)
fulano.set_salary(4500)
fulano.show_details()
ciclano.set_salary(10900)
ciclano.show_details()

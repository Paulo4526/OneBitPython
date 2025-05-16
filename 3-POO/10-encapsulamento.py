class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary #"__" modifica o atributo para private

    def show_details(self):
        print(f"\nNome: {self.name} \nSalary: {self.__salary}\n")

    def alter_salary(self, newSalary):
        self.__salary = newSalary

paulo = Employee("Paulo", 5000)
carlos = Employee("Carlos", 6000)
paulo.alter_salary(4500)
paulo.show_details()
carlos.show_details()
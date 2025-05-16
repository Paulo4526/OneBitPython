from pai import Animal
class Lion(Animal):
    __mane = ""

    def get_mane(self):
        return self.__mane
    def set_mane(self, mane):
        self.__mane = mane

    def show_details(self):
        print(f"A juba do animal é {self.get_mane()} \nRaça {Animal.get_name(self)} \nTamanho: {Animal.get_size(self)} \nCor: {Animal.get_color(self)}\n")
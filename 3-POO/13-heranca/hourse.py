from pai import Animal

class Horse(Animal):
    __race = ""
    def get_race(self):
        return self.__race

    def set_race(self, race):
        self.__race = race

    def show_datails(self):
        print(f"Raça do cavalo é {self.get_race()}  \nRaça {Animal.get_name(self)} \nTamanho: {Animal.get_size(self)} \nCor: {Animal.get_color(self)}\n")
from zoo import Zoo
from fish_filho import Fish
from parrots_filho import Parrot

#Criando a composição na classe Zoo
def main():
    zoo = Zoo()
    fish = Fish("Nemo", "mamíferos")
    print(vars(fish))
    parrot = Parrot("Louro", "aves")
    print(vars(parrot))

    zoo.add_animal(fish)
    print(zoo.total_of_category("mamíferos"))

    zoo.add_animal(parrot)
    print(zoo.total_of_category("aves"))


if __name__ == "__main__":
    main()

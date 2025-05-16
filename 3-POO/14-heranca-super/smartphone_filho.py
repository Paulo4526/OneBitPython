from phone_pai import Phone #Importando a classe pai

class Smartphone(Phone):#Atribuindo a classe pai "Phone" à classe filha
    def __init__(self, brand, model, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model, model_name, price) #Atribuindo valores a classe pai
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera

    def show_details(self):
        print(f"\nMarca: {self._brand}")
        print(f"Modelo: {self._model}")
        print(f"Nome do Modelo: {self._model_name}")
        print(f"Preço: {self._price}")
        print(f"Memoria Ram: {self.ram}")
        print(f"Memoria Interna: {self.internal_memory}")
        print(f"Câmera Traseira: {self.back_camera}")
        #OBS: Sempre adicionar a representação correta do valor se for seguro com 1 underscore e privado 2 udnerscore
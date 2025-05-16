"""
1 - O metodo de classe utiliza o parametro referente a vlasse
2 - O metodo de classe pode acessar ou modificar o estado da classe
3 - Usamos o decorator @classmethod para criar um metodo de classe
"""
class Console:
    def __init__(self, name, price): #Criando o construtor
        self.name = name
        self.price = price

    @classmethod
    def from_text(cls, string): #cls é uma referencia a nossa classe, e a string o tipo de entrada do metodo
        import re #Módulo re nativo do python
        item = re.findall(r' é \w+', string)
        name = item[0][3:]
        price = item[1][3:]
        return cls(name, price)

wiiU = Console.from_text("Meu vide game é WiiU e o preço é 1000 reais")
xbox = Console.from_text("Meu vídeo game é XboxOne e o preço é 1500 reais")
print(wiiU.__dict__) #Transforma em dicionário
print(xbox.__dict__) #Transforma em dicionário
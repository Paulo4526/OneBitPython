class Produto:
    def __init__(self, nome, preco, marca):
        self.nome = nome
        self.preco = preco
        self.marca = marca
        self.avaliacoes = 0
        self.notaAvaliacoes = 0
        self.valorDesc = 0

    def __str__(self):
        return f'\nNome: {self.nome} \nPreço: {self.preco} \nMarca: {self.marca} \nAvaliações: {self.avaliacoes}'

    def descricao_produto(self):
        print(f"Nome: {self.nome}")
        if self.valorDesc == 0:
            print(f"Preço do Produto: {self.preco:.2f}")
        elif self.valorDesc >= self.preco:
            print(f"Preço do Produto: {self.preco:.2f}")
        else:
            print(f"De: {self.preco:.2f}R$ \nPor: {self.valorDesc:.2f}R$")
        print(f"Marca: {self.marca}")
        if self.avaliacoes == 0:
            print(f"Avaliações: Este produto ainda não foi avaliado")
        else:
            print(f"Total de Avaliações: {self.avaliacoes}")


    def avaliacao(self, nota):
        self.notaAvaliacoes += nota
        self.avaliacoes += 1

    def desconto(self, desc): #Inserir valor que deseja dar desconto em % sendo 0.1 À 100
        self.valorDesc = self.preco * (1 - (desc / 100))

    def aumentoPreco(self, aumento):
        if aumento > 100:
            self.preco *= (aumento / 100)
        else:
            self.preco *= (1 + (aumento / 100))

    def avarage(self):
        print(f"\nNota Avaliação {self.nome}: {self.notaAvaliacoes / self.avaliacoes}")

televisao = Produto("TV 45'' Smart + Netflix", 5620.99, "Samsung")
televisao.aumentoPreco(0.33)
televisao.descricao_produto()

geladeira = Produto("Geladeira Fros-Free 2 espaços inverter", 554.23, "Brastemp")
geladeira.avaliacao(10.0)
geladeira.avaliacao(5.0)
geladeira.desconto(23.55)
geladeira.avarage()
geladeira.descricao_produto()


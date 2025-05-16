"""
1 - O metodo statico nao utiliza o parametro referente a classe
2- O metodo estatico pode acessar mas nao pode modificar o estado da classe
3 - Usamos o decorator @staticmethod para criar um metodo estatico
"""
class Course:
    def __init__(self, nome, trail):
        self.nome = nome
        self.trail = trail

    @staticmethod
    def couser_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando Python", "Módulos e PIP", "Programação Orientada à Objetos"]
        elif trail == "Automação com o Python":
            courses = ["Automação de Tarefas", "Web Scraping", "Assistente Virtual em Python"]
        else:
            courses = ["A definir"]
        return courses

print(Course.couser_trail("Automação com o Python"))
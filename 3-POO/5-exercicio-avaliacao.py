class Movie: #Novamente criamos a classe Movie
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes): #Criando o construtor para que seja compartilhado em outras classes
        self.name = name #Self equivale ao this em Java
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalNote = 0
        self.totalEvaluator = 0
        self.durationMinutes = durationMinutes
        #OBS: Aqui não estamos criando 1 construtor vazio e sim com valores pré-fefinidos

    def __str__(self): #Metodo especial __self__
        return f"Filme {self.name} \nAno de Lançamento {self.yearLaunch} \nIncluso no Plano?: {self.includedPlan} \nNota: {self.note} \nTempo de Ruação: {self.durationMinutes}\n"
    #OBS: O metodo __self__ tem a mesma função que o toString em java.

    def techinical_sheet(self): #Metodo onde resgatamos os valores salvos de cada filme
        print("\n------------------------------------------")
        print(f"#Nome do Filme {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Filme incluso no plano?: {self.includedPlan} ")
        print(f"Total de Avaliações: {self.totalEvaluator}")
        print(f"Duração em minutos: {self.durationMinutes}")

    def evaluate(self, note):
        self.totalNote += note
        self.totalEvaluator += 1

    def average(self):
        print(f"Média do filme {self.name}: {self.totalNote/self.totalEvaluator}")

mario = Movie("Mario Bross", 2023, True, 180)
avatar = Movie("Avatar", 2024, True, 220)
mario.evaluate(10.0)
mario.evaluate(8.0)
mario.evaluate(4.0)
avatar.evaluate(9.2)
avatar.evaluate(5.3)
avatar.evaluate(5.0)

mario.techinical_sheet()
mario.average()
avatar.techinical_sheet()
avatar.average()


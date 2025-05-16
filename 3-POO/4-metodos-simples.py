class Movie: #Novamente criamos a classe Movie
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes): #Criando o construtor para que seja compartilhado em outras classes
        self.name = name #Self equivale ao this em Java
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
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
        print(f"Nota: {self.note}")
        print(f"Duração em minutos: {self.durationMinutes}")

mario = Movie("Super Mario Bross", 2023, False, 5.0, 180)
top_fun = Movie("Top Gun - Maverik", 2022, True, 4.9, 220)
mario.techinical_sheet() #Chamando o metodo através da instancia mario
top_fun.techinical_sheet() #Chamando o metodo através da instância top_fun
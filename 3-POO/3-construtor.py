class Movie: #Novamente criamos a classe Movie
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes): #Criando o construtor para que seja compartilhado em outras classes
        self.name = name #Self equivale ao this em Java
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
        #OBS: Aqui não estamos criando 1 construtor vazio e sim com valores pré-fefinidos

    def __str__(self):
        return f"Filme {self.name} \nAno de Lançamento {self.yearLaunch} \nIncluso no Plano?: {self.includedPlan} \nNota: {self.note} \nTempo de Ruação: {self.durationMinutes}\n"
    #OBS: O metodo __self__ tem a mesma função que o toString em java.

#Instanciando a classe e criando objeto
movie = Movie("Duro de Matar", 1991, True, 5, 180)
print(movie) #Quando chamarmos somente a instância será automaticamente chamado o metodo __self__
print(f"Dados do filme {movie.name}:")
print(f"Ano de Lançamento: {movie.yearLaunch} \nIncluso no Plano?: {movie.includedPlan} \nNota: {movie.note} \nTempo de Duração: {movie.durationMinutes}")
class Movie: #Aqui criamos nossa classe
    name = "" #Defininto atributo nome
    yearLounch = 0 #Definindo atributo de ano de lançamento
    includedPlan = False #Definindo atributo caso o filme está incluso no plano
    note = 0 #Definindo o atributo de nota fo filme
    durationMinutes = 0 #Definindo o atributo de duração do filme

#Instanciando e criando 1 objeto
movie = Movie() #Criando a instancia da classe Movie e abaixo atribuindo valores aos atributos da classe Movie
movie.name = "Duro de Matar"
movie.yearLaunch = 1998
movie.includedPlan = True
movie.note = 5
movie.durationMinutes = 180
print(movie)
print(f"Dados do filme {movie.name}:")
print(f"Ano de Lançamento: {movie.yearLaunch} \nIncluso no Plano?: {movie.includedPlan} \nNota: {movie.note} \nTempo de Duração: {movie.durationMinutes}")
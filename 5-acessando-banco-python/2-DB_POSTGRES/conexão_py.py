import psycopg2 as psy

#Primeiramente instalar o psycopg2
#comando no terminal pip install psycopg2

connect = psy.connect(
    database = 'onebit', #banco de dados criado no docker ou pela interface do postgres
    user = 'admin', #Usuario criado na instalação do banco ou imagem docker
    password = '123', #Senha criada na instalação do banco ou imagem docker
    host = 'localhost', #Host local da sua maquina criado na instalação ou pelo docker
    port = '5432' #Posrta padrão do postgress, se for com docker poderá sofrer alterações
)
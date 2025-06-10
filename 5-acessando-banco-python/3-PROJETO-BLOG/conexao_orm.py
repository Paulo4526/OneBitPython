#primeiramente instalar a biblioteca alchemy com o comando"pip install sqlalchemy"
#importar a biblioteca engine, sessionmaker e declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#Criando conexão com banco de dados
API =  'postgresql' #informando qual banco será usado se postgres, mysql e etc.
user = 'admin' #nome do usuário do banco
password = '123' #senha do usuario
host = 'localhost' #host
database = 'onebit'#Banco de dados
#Criando a url para acessar nosso banco de dados
DATABASE_URI = f"{API}://{user}:{password}@{host}:5432/{database}"


#Criando a engine
newEngine = create_engine(DATABASE_URI)

#Criando a sessão
Session = sessionmaker(bind=newEngine)
session = Session()

#Criando a base
Base = declarative_base()



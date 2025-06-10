from conexao_orm import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    #Criando a tabela com ORM
    __tablename__ = 'T_SIP_USERS'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    posts = relationship('Post', back_populates='author')

    #Iniciando a classe
    def __init__(self, name, email):
        self.name = name
        self.email = email
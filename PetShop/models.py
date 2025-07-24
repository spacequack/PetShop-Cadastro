from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base



# cria o banco de dados SQLite
db  = create_engine('sqlite:///animals.db')

# cria a base para os modelos do sqlachemy
Base = declarative_base()


# classes/tabelas do banco de dados
class Animal(Base):
    __tablename__ = 'animals'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    idade = Column('idade', Integer, nullable=False)
    especie = Column('especie', String, nullable=False)
    sexo = Column('sexo', String, nullable=False)
    cor = Column('cor', String, nullable=False)

    def __init__(self, nome, idade, especie, sexo, cor):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.sexo = sexo
        self.cor = cor


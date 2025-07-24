from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Animal
from schemas import SchemaAnimal
from dependencies import catch_session



app = FastAPI()


# rotas
@app.get("/")
async def home():
    '''
    Rota inicial
    '''
    return {"message": "Bem-vindo ao sistema de gerenciamento de animais!"}


@app.get("/list")
async def list_animals(session: Session = Depends(catch_session)):
    '''
    rota para listar animais
    '''
    animal = session.query(Animal).all()
    return {"Animais": animal}


@app.get("/search/{animal_id}")
async def search_animal(animal_id: int, session: Session = Depends(catch_session)):
    '''
    rota para buscar um animal pelo ID
    '''
    
    animal = session.query(Animal).filter(Animal.id == animal_id).first()
    
    if not animal:
        return {"message": "Animal não encontrado!"}
    return {"Animal": animal}


@app.post("/create")
async def create_animal(animal: SchemaAnimal, session: Session = Depends(catch_session)):
    '''
    rota para criar um animal
    '''
    
    existing_animal = session.query(Animal).filter(Animal.nome == animal.nome).first()
    
    if existing_animal:
        return {"message": "Animal já existe!"}
    
    new_animal = Animal(
        nome=animal.nome, 
        idade=animal.idade, 
        especie=animal.especie, 
        sexo=animal.sexo, 
        cor=animal.cor
    )
    session.add(new_animal)
    session.commit()
    return {"message": f"Animal Registrado com sucesso {animal.nome}"}

    


@app.post("/delete/{animal_id}")
async def delete_animal(animal_id: int, session: Session = Depends(catch_session)):
    '''
    rota para deletar um animal pelo ID
    '''

    animal = session.query(Animal).filter(Animal.id == animal_id).first()
    
    if not animal:
        return {"message": "Animal não encontrado!"} 

    session.delete(animal)
    session.commit()
    return {"message": "Animal deletado com sucesso!"}
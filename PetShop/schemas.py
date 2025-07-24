from pydantic import BaseModel

# define o schema do animal
class SchemaAnimal(BaseModel):
    nome: str
    idade: int
    especie: str
    sexo: str
    cor: str

    class Config:
        from_attributes = True
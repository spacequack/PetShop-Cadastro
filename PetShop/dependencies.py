from sqlalchemy.orm import sessionmaker, Session
from models import Base, db

Base.metadata.create_all(bind=db)

# Cria a sessão do banco de dados
def catch_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
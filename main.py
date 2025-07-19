from sqlmodel import SQLModel

from models import create_tonnage, create_dct, create_flux
from db import engine 

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
    create_dct()
    create_flux()
    create_tonnage()

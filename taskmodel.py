from sqlmodel import Field, SQLModel, Session, Relationship, select

from datetime import datetime

from db import engine
from models import EnumDct

class Task(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    task : str
    description : str
    created_at : datetime = Field(default_factory=datetime.now)
    dct : EnumDct
    finish : bool = Field(default=False)
    finished_at : datetime | None=None
    model_config = {"validate_assignment": True} # Permet de valider la donnée avec Pydantic à l'instanciation


def create_tasks():
    task_1 = Task(task = 'Task test1', description='test desciption1',  dct="Belz")
    task_2 = Task(task = 'Task test2', description='test desciption2',  dct="Crach", finish=True)
    task_3 = Task(task = 'Task test3', description='test desciption3',  dct="Saint-Anne")
    
    with Session(engine) as session:
        session.add(task_1)
        session.add(task_2)
        session.add(task_3)
        
        session.commit()

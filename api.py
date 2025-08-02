from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from typing import Annotated, List

from db import engine
from models import Tonnage
from taskmodel import Task
from readmodels import TonnageRead, DctRead

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#*********************** Définition des routes **********************
@app.get("/")
async def root():
    return {"message": "Hello World"}

#Retourne les tonnages de toutes les dct
@app.get("/tonnages/", response_model=List[TonnageRead])
def read_tonnages(session: Session = Depends(get_session)):
    statement = select(Tonnage).options(selectinload(Tonnage.dct), selectinload(Tonnage.flux))
    results = session.exec(statement).all()
    return results

#Retourne les tonnages avec l'année en paramètres de la requête
@app.get("/tonnages/{year}", response_model=List[TonnageRead])
async def get_tonnage_year(year: int, session: Session = Depends(get_session)):
    statement = select(Tonnage).where(Tonnage.year == year)
    results = session.exec(statement).all()
    return results

#Retourne toutes les tâches
@app.get("/tasks")
async def get_tasks(session: Session =Depends(get_session)):
    return session.exec(select(Task)).all()

#Post task
@app.post("/tasks", response_model=Task)
async def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

#Supprime task
@app.delete("/tasks/{id}")
async def delete_task(id: int, session: Session = Depends(get_session)):
    task = session.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Tâche introuvable")   
    
    session.delete(task)
    session.commit()
    return {"message": f"Tâche {id} supprimée"}

#MAJ task 
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: Task, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")

    # Appliquer les changements uniquement sur les champs fournis
    task_data = task_update.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)

    return task
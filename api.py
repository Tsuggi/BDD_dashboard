from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from typing import Annotated, List

from db import engine
from models import Tonnage
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



from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select
from db import engine
from typing import Annotated
from models import Tonnage

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tonnages/")
def read_tonnages(session: SessionDep) -> list[Tonnage]:
    tonnages = session.exec(select(Tonnage)).all()
    return tonnages
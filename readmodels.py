from sqlmodel import SQLModel
from models import EnumMonth, EnumDct, EnumFlux

class DctRead(SQLModel):
    dct: EnumDct

class FluxRead(SQLModel):
    flux: EnumFlux

class TonnageRead(SQLModel):
    year: int
    month: EnumMonth
    tonnage: float
    dct: DctRead
    flux: FluxRead
    
    
from enum import Enum
from sqlmodel import Field, SQLModel, Session, Relationship, select
from db import engine
from data import data_test

class EnumMonth(str, Enum):
        janvier = "Janvier"
        fevrier = "Février"
        mars = "Mars"
        avril = "Avril"
        mai = "Mai"
        juin = "Juin"
        juillet = "Juillet"
        aout = "Août"
        septembre = "Septembre"
        octobre = "Octobre"
        novembre = "Novembre"
        decembre = "Décembre"
class EnumDct(str, Enum):
        belz = "Belz"
        carnac = "Carnac"
        crach = "Crach"
        saint_anne = "Saint-Anne"
        pluvigner = "Pluvigner"
        quiberon = "Quiberon"
class EnumFlux(str, Enum):
        non_valorisable = "Non valorisable"
        valorisation_energetique = "Valorisation energétique"
        dechets_verts = "Déchets verts"
        carton = "Carton"
        piles = "Piles"
        huiles_minerales = "Huiles minérales"
        eco_dds = "EcoDDS"
        dds = "DDS"
        platre = "Plâtre"
        gravats = "Gravats"
        metaux = "Métaux"
        plastique_pmcb = "Plastiques PMCB"
        mobilier_melange = "Mobilier en mélange"
        bois_pmcb = "Bois PMCB"
        bois = "Bois"
        menuiseries_vitrees = "Menuiseries vitrées"
        deee = "DEEE"
        neons = "Néons"
        lampes = "Lampes"
        cartouches = "Cartouches"
        briques_platrieres = "Briques plâtrières"
        pneus = "Pneus"
        pneus_aliapur = "Pneus Aliapur"
        asl = "Articles de Sport et Loisirs"
        batteries = "Batteries"


class Dct(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    dct : EnumDct
    
    tonnages: list["Tonnage"] = Relationship(back_populates="dct")

    model_config = {"validate_assignment": True} # Permet de valider la donnée avec Pydantic à l'instanciation
class Flux(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    flux : EnumFlux
    fluxes: list["Tonnage"] = Relationship(back_populates="flux")
    
    model_config = {"validate_assignment": True} # Permet de valider la donnée avec Pydantic à l'instanciation
class CoutUnitaireTransport(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    cout_unitaire : int
    year : int
    month : EnumMonth
    model_config = {"validate_assignment": True} # Permet de valider la donnée avec Pydantic à l'instanciation
class CoutUnitaireTraitement(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    cout_unitaire : int
    year : int
    month : EnumMonth
    model_config = {"validate_assignment": True} # Permet de valider la donnée avec Pydantic à l'instanciation
class Tonnage(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    year : int
    month : EnumMonth
    tonnage : float 
    cout_unitaire_transport : int | None = Field(default=None, foreign_key="coutunitairetransport.id")
    cout_unitaire_traitement : int | None = Field(default=None, foreign_key="coutunitairetraitement.id")
    
    flux_id : int = Field(foreign_key="flux.id")
    flux: Flux = Relationship(back_populates="fluxes")
    
    dct_id : int = Field(foreign_key="dct.id")
    dct: Dct = Relationship(back_populates="tonnages")

    model_config = {"validate_assignment": True} # Permet de valider la donnée avec Pydantic à l'instanciation


def create_dct():
    dct_belz = Dct(dct="Belz")
    dct_crach = Dct(dct="Crach")
    dct_carnac = Dct(dct="Carnac")
    dct_quiberon = Dct(dct="Quiberon")
    dct_saintanne = Dct(dct="Saint-Anne")
    dct_pluvigner = Dct(dct="Pluvigner")


    with Session(engine) as session:
        session.add(dct_belz)
        session.add(dct_carnac)
        session.add(dct_crach)
        session.add(dct_quiberon)
        session.add(dct_pluvigner)
        session.add(dct_saintanne)
        
        session.commit()

def create_flux():
    flux_non_valorisable = Flux(flux="Non valorisable")
    flux_valorisation_energetique = Flux(flux="Valorisation energétique")
    flux_dechets_verts = Flux(flux="Déchets verts")
    flux_carton = Flux(flux="Carton")
    flux_piles = Flux(flux="Piles")
    flux_huiles_minerales = Flux(flux="Huiles minérales")
    flux_eco_dds = Flux(flux="EcoDDS")
    flux_dds = Flux(flux="DDS")
    flux_platre = Flux(flux="Plâtre")
    flux_gravats = Flux(flux="Gravats")
    flux_metaux = Flux(flux="Métaux")
    flux_plastique_pmcb = Flux(flux="Plastiques PMCB")
    flux_mobilier_melange = Flux(flux="Mobilier en mélange")
    flux_bois_pmcb = Flux(flux="Bois PMCB")
    flux_bois = Flux(flux="Bois")
    flux_menuiseries_vitrees = Flux(flux="Menuiseries vitrées")
    flux_deee = Flux(flux="DEEE")
    flux_neons = Flux(flux="Néons")
    flux_lampes = Flux(flux="Lampes")
    flux_cartouches = Flux(flux="Cartouches")
    flux_briques_platrieres = Flux(flux="Briques plâtrières")
    flux_pneus = Flux(flux="Pneus")
    flux_pneus_aliapur = Flux(flux="Pneus Aliapur")
    flux_asl = Flux(flux="Articles de Sport et Loisirs")
    flux_batteries = Flux(flux="Batteries")
    
    with Session(engine) as session:
        session.add(flux_non_valorisable)
        session.add(flux_valorisation_energetique)
        session.add(flux_dechets_verts)
        session.add(flux_carton)
        session.add(flux_piles)
        session.add(flux_huiles_minerales)
        session.add(flux_eco_dds)
        session.add(flux_dds)
        session.add(flux_platre)
        session.add(flux_gravats)
        session.add(flux_metaux)
        session.add(flux_plastique_pmcb)
        session.add(flux_mobilier_melange)
        session.add(flux_bois_pmcb)
        session.add(flux_bois)
        session.add(flux_menuiseries_vitrees)
        session.add(flux_deee)
        session.add(flux_neons)
        session.add(flux_lampes)
        session.add(flux_cartouches)
        session.add(flux_briques_platrieres)
        session.add(flux_pneus)
        session.add(flux_pneus_aliapur)
        session.add(flux_asl)
        session.add(flux_batteries)
        
        session.commit()

def create_tonnage():
    with Session(engine) as session:
        for data in data_test:
            tonnage_test = Tonnage(
                year = 2023, 
                month = data['mois'], 
                tonnage= data['tonnage'], 
                flux = session.exec(select(Flux).where(Flux.flux == data['flux'])).first(), 
                dct = session.exec(select(Dct).where(Dct.dct == data['dct'])).first()
            )
            session.add(tonnage_test)
        
        session.commit()

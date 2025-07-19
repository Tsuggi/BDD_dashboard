import json 

with open("tonnages2023.json", "r") as f: 
    data_tonnage2023 = json.load(f)

data_test = [
    {'mois' : 'Janvier', 'dct' : 'Saint-Anne', 'flux' : 'Gravats', 'tonnage' : 5},
    {'mois' : 'Février', 'dct' : 'Saint-Anne', 'flux' : 'Huiles minérales', 'tonnage' : 5},
    {'mois' : 'Mars', 'dct' : 'Carnac', 'flux' : 'Déchets verts', 'tonnage' : 10},
    {'mois' : 'Janvier', 'dct' : 'Belz', 'flux' : 'Gravats', 'tonnage' : 15},
    {'mois' : 'Janvier', 'dct' : 'Crach', 'flux' : 'Gravats', 'tonnage' : 65},
]
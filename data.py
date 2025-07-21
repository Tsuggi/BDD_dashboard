import json 

with open("tonnages2023.json", "r") as f: 
    data_tonnage2023 = json.load(f)

data_test = [
    {'mois': 'Janvier', 'dct': 'Saint-Anne', 'flux': 'Gravats', 'tonnage': 5, 'year': 2024},
    {'mois': 'Février', 'dct': 'Saint-Anne', 'flux': 'Huiles minérales', 'tonnage': 5, 'year': 2023},
    {'mois': 'Mars', 'dct': 'Carnac', 'flux': 'Déchets verts', 'tonnage': 10, 'year': 2024},
    {'mois': 'Janvier', 'dct': 'Belz', 'flux': 'Gravats', 'tonnage': 15, 'year': 2023},
    {'mois': 'Juillet', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2024},
    {'mois': 'Décembre', 'dct': 'Crach', 'flux': 'Déchets verts', 'tonnage': 55, 'year': 2023},
    {'mois': 'Octobre', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2023},
    {'mois': 'Novembre', 'dct': 'Carnac', 'flux': 'Gravats', 'tonnage': 65, 'year': 2024},
    {'mois': 'Avril', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2023},
    {'mois': 'Mai', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2024},
    {'mois': 'Juin', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2024},
    {'mois': 'Août', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2023},
    {'mois': 'Septembre', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2023},
    {'mois': 'Janvier', 'dct': 'Crach', 'flux': 'Gravats', 'tonnage': 65, 'year': 2024},
]
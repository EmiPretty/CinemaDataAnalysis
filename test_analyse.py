import sys
import pandas as pd
import matplotlib
import tkinter
matplotlib.use('TkAgg')  # Spécifie le backend graphique pour macOS
import matplotlib.pyplot as plt

# Ajout du dossier 'src' au chemin d'importation
sys.path.append('./src')

# Importation des fonctions depuis le module 'analyse'
from analyse import calculate_mean_entries, plot_top_regions

# Définition des données sous forme de dictionnaire
cinema_data = {
    'région administrative': [
        'Île-de-France', 'Provence-Alpes-Côte d\'Azur', 'Occitanie', 
        'Auvergne-Rhône-Alpes', 'Nouvelle-Aquitaine',
        'Bourgogne-Franche-Comté', 'Bretagne', 'Centre-Val de Loire',
        'Grand Est', 'Hauts-de-France'
    ],
    'écrans': [200, 150, 180, 220, 170, 130, 140, 160, 190, 210],
    'fauteuils': [5000, 4000, 4500, 6000, 5200, 3100, 3400, 4200, 4700, 5100],
    'entrées 2021': [500000, 400000, 450000, 550000, 520000, 300000, 320000, 400000, 470000, 500000],
    'entrées 2022': [520000, 420000, 470000, 580000, 530000, 310000, 330000, 410000, 480000, 510000]
}

# Création du DataFrame à partir du dictionnaire de données
df = pd.DataFrame(cinema_data)

# Calcul des moyennes des entrées pour les années 2021 et 2022
moyennes_entrées_2021, moyennes_entrées_2022 = calculate_mean_entries(df)

print("Moyennes des entrées par région en 2021 :\n", moyennes_entrées_2021)
print("Moyennes des entrées par région en 2022 :\n", moyennes_entrées_2022)
plot_top_regions(moyennes_entrées_2021, moyennes_entrées_2022)

from nettoyage import charger_donnees, nettoyer_donnees
from analyse import calculer_moyenne_entrees, afficher_meilleurs_regions
from modelisation import entrainer_modele, evaluer_modele
from utilitaires import preparer_donnees
import pandas as pd

chemin_fichier = "data/cinemas.csv"

# Chargement des données depuis le fichier
donnees = charger_donnees(chemin_fichier)

# Nettoyage des données pour éliminer les anomalies
donnees_nettoyees = nettoyer_donnees(donnees)

# Calcul des moyennes des entrées par commune pour les années 2021 et 2022
moyennes_2021, moyennes_2022 = calculer_moyenne_entrees(donnees_nettoyees)

# Affichage des résultats des moyennes pour chaque année
print("Moyennes des entrées par commune en 2021 :\n", moyennes_2021)
print("Moyennes des entrées par commune en 2022 :\n", moyennes_2022)

# Affichage des graphiques des régions ayant les meilleures performances
afficher_meilleurs_regions(moyennes_2021, moyennes_2022)

# Préparation des données pour l'entraînement et le test du modèle
X_entrainement, X_test, y_entrainement, y_test = preparer_donnees(donnees_nettoyees)

# Entraînement du modèle en utilisant les données d'entraînement
modele = entrainer_modele(X_entrainement, y_entrainement)

# Évaluation des performances du modèle sur les données de test
r2, mae = evaluer_modele(modele, X_test, y_test)

# Affichage des résultats d'évaluation du modèle
print(f"Performance du modèle - R² : {r2}, MAE : {mae}")

# Création de données fictives pour effectuer une prédiction
ecrans_fictifs = 5
fauteuils_fictifs = 500
population_fictive = 10000

# Création d'un DataFrame avec ces données fictives
donnees_fictives = pd.DataFrame([[ecrans_fictifs, fauteuils_fictifs, population_fictive]],
                                columns=['écrans', 'fauteuils', 'population de la commune'])

# Utilisation du modèle pour prédire les entrées basées sur ces données fictives
entrees_predites = modele.predict(donnees_fictives)

print(f"Prédiction des entrées pour les données fictives : {entrees_predites[0]}")

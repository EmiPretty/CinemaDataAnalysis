import pandas as pd
from src.nettoyage import load_data, clean_data, display_statistics
from src.analyse import calculate_mean_entries, plot_top_regions
from src.modelisation import train_model, evaluate_model
from utilitaires import prepare_data

fichier_donnees = "data/cinemas.csv"

# Charger et nettoyer les données
df_donnees = load_data(fichier_donnees)
df_sans_valeurs_manquantes = clean_data(df_donnees)

# Afficher les statistiques descriptives sur les données nettoyées
display_statistics(df_sans_valeurs_manquantes)

# Calcul des moyennes des entrées pour les années 2021 et 2022 par région
moyennes_entrées_2021, moyennes_entrées_2022 = calculate_mean_entries(df_sans_valeurs_manquantes)

# Visualiser les entrées moyennes par région pour les deux années
plot_top_regions(moyennes_entrées_2021, moyennes_entrées_2022)

# Préparation des données pour l'entraînement du modèle
X_entraînement, X_test, y_entraînement, y_test = prepare_data(df_sans_valeurs_manquantes)

# Entraîner un modèle de régression linéaire sur les données d'entraînement
modele = train_model(X_entraînement, y_entraînement)

# Évaluer les performances du modèle sur le jeu de test
coefficient_r2, erreur_absolue_moyenne = evaluate_model(modele, X_test, y_test)
print(f"R² : {coefficient_r2}, MAE : {erreur_absolue_moyenne}")

# Définir des valeurs fictives pour la prédiction
nombre_ecrans_fictifs = 5
nombre_fauteuils_fictifs = 500
population_fictive = 10000

prediction_entrées_fictives = modele.predict([[nombre_ecrans_fictifs, nombre_fauteuils_fictifs, population_fictive]])
print(f"Prédiction des entrées pour les données fictives : {prediction_entrées_fictives}")

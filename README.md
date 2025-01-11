### Analyse des Données Cinématographiques

# Ce projet a pour objectif d’étudier l’impact des infrastructures des cinémas français (nombre d’écrans et de fauteuils) sur la fréquentation.
# L’analyse cherche à dégager des insights permettant d'améliorer la fréquentation des cinémas et de créer un modèle prédictif pour estimer les entrées annuelles en fonction des infrastructures présentes.

## Structure du projet
# src/ : Dossier contenant les scripts Python pour le traitement des données, l’analyse et la modélisation.
# nettoyage.py : Chargement et nettoyage des données.
# analyse.py : Fonctions pour les calculs statistiques et les visualisations.
# modelisation.py : Scripts pour entraîner et tester le modèle prédictif.
# utilitaires.py : Fonctions auxiliaires (préparation des données, etc.).
# donnees/ : Contient le fichier CSV des données (cinemas.csv).
# README.md : Ce fichier, incluant la documentation et les réponses aux questions du projet.
# requirements.txt : Liste des dépendances Python.

## Données fournies
# Le fichier cinemas.csv contient plusieurs colonnes :
# region : Région administrative du cinéma.
# commune : Nom de la commune.
# population_commune : Population de la commune.
# ecrans : Nombre d’écrans du cinéma.
# fauteuils : Nombre total de fauteuils.
# annee : Année de collecte des données (2018 à 2022).
# entrees_annuelles : Nombre total d'entrées pour l'année correspondante.
# label_art_et_essai : Indication si le cinéma a un label Art et Essai (oui/non).

# 1. Nettoyage et Exploration des Données
# Nettoyage
# Chargement des données :
# Le fichier CSV est chargé dans un DataFrame pandas.
# Traitement des valeurs manquantes :
# Les valeurs manquantes dans la colonne entrees_annuelles ont été remplacées par la moyenne des entrées de la même région.
# Les lignes contenant des valeurs aberrantes (comme des nombres d’écrans ou fauteuils égaux à zéro) ont été supprimées.
# Justification :
# Les valeurs manquantes ont été corrigées pour garantir la cohérence des analyses, et les anomalies ont été supprimées pour éviter toute distorsion dans les résultats.

# Exploration
# Aperçu des données :
# Les 5 premières lignes du DataFrame ont été affichées pour un premier contrôle.
# Des statistiques descriptives ont été calculées pour les colonnes numériques :
# Nombre moyen d’écrans : 150.
# Nombre moyen de fauteuils : 4 200.
# Entrées annuelles moyennes : 400 000.

# 2. Analyse des Données
# Résultats principaux
# Entrées moyennes par fauteuil en 2022 :
# Ces valeurs ont été calculées pour chaque région.
# Top 3 des régions avec les meilleures entrées par fauteuil :
# Provence-Alpes-Côte d'Azur : 105 entrées par fauteuil.
# Île-de-France : 100 entrées par fauteuil.
# Auvergne-Rhône-Alpes : 95 entrées par fauteuil.
# Pires régions (entrées moyennes par fauteuil) :
# Bretagne : 69 entrées par fauteuil.
# Centre-Val de Loire : 72 entrées par fauteuil.
# Bourgogne-Franche-Comté : 75 entrées par fauteuil.
# Visualisation :
# Un graphique à barres des 10 régions avec les meilleures et les pires performances en termes d'entrées par fauteuil a été généré.

# 3. Corrélation entre Infrastructures et Fréquentation
# Corrélation entre le nombre d'écrans et les entrées annuelles :
# Le coefficient de corrélation est de 0.89, ce qui montre une forte relation positive.
# Corrélation entre le nombre de fauteuils et les entrées annuelles :
# Le coefficient de corrélation est de 0.86, ce qui indique également une forte relation positive.
# Conclusion :
# Le nombre d’écrans a une influence légèrement plus marquée sur la fréquentation que le nombre de fauteuils.
# Visualisation :
# Deux nuages de points avec régression linéaire ont été créés pour visualiser la relation entre ces variables et les entrées annuelles.

# 4. Modèle Prédictif des Entrées Annuelles
# Entraînement et Évaluation
# Variables utilisées :
# Variables explicatives : ecrans, fauteuils, population_commune.
# Variable cible : entrees_annuelles.
# Performance du modèle :
# Le modèle a un coefficient de détermination (R²) de 0.92, ce qui indique une bonne capacité à expliquer la variance des entrées annuelles.
# L'erreur moyenne absolue (MAE) est de 25 000 entrées.
# Prédiction pour 2022 :
# Les prédictions du modèle ont été comparées aux données réelles, avec un écart moyen inférieur à 5%, indiquant une très bonne précision.

# 5. Recommandations Stratégiques
# Cas d'une commune fictive
# Situation initiale :
# Population : 20 000 habitants.
# 2 écrans et 120 fauteuils.
# Entrées prédites : 10 000.
# Scénarios testés :
# Augmentation à 5 écrans :
# Entrées prédites : 18 000.

# Installation
# Clonez ce projet avec la commande :
# git clone https://github.com/EmiPretty/CinemaDataAnalysis.git
# cd CinemaDataAnalysis
# Créez un environnement virtuel :
# python3 -m venv myenv
# source myenv/bin/activate
# Installez les dépendances :
# pip install -r requirements.txt
# pip install --upgrade scikit-learn seaborn
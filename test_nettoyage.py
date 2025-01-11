from nettoyage import charger_donnees, nettoyer_donnees, afficher_statistiques

chemin_fichier = "data/cinemas.csv"

# Chargement des données depuis le fichier CSV
donnees = charger_donnees(chemin_fichier)

# Affichage d'un aperçu des premières lignes des données pour vérifier leur contenu
print("Aperçu des premières lignes des données :\n", donnees.head())

# Nettoyage des données pour éliminer les valeurs manquantes et les anomalies
donnees_nettoyees = nettoyer_donnees(donnees)

# Affichage des données après nettoyage pour vérifier les modifications
print("Données après nettoyage :\n", donnees_nettoyees.head())

afficher_statistiques(donnees_nettoyees)

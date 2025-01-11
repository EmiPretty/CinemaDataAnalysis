import pandas as pd
from sklearn.model_selection import train_test_split
from modelisation import train_model, evaluate_model

# Création d'un jeu de données d'exemple avec des informations sur les cinémas
cinema_data = {
    'nombre d\'écrans': [200, 150, 180, 220, 170],
    'nombre de fauteuils': [5000, 4000, 4500, 6000, 5200],
    'population de la commune': [100000, 80000, 90000, 120000, 95000],
    'entrées 2022': [520000, 420000, 470000, 580000, 530000]
}

# Conversion des données en un DataFrame pandas pour faciliter l'analyse
df_cinemas = pd.DataFrame(cinema_data)

# Définition des variables explicatives (X) et de la variable cible (y)
X = df_cinemas[['nombre d\'écrans', 'nombre de fauteuils', 'population de la commune']]
y = df_cinemas['entrées 2022']

# Séparation des données en un ensemble d'entraînement (80%) et un ensemble de test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle de prédiction avec les données d'entraînement
trained_model = train_model(X_train, y_train)

# Évaluation du modèle avec les données de test pour obtenir les performances
r_squared, mae = evaluate_model(trained_model, X_test, y_test)

print(f"Coefficient de détermination (R²) : {r_squared}")
print(f"Erreur absolue moyenne (MAE) : {mae}")

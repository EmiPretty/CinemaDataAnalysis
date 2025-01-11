import pandas as pd
from sklearn.model_selection import train_test_split

def pretraiter_donnees(df):
    colonnes_necessaires = ['écrans', 'fauteuils', 'population de la commune', 'entrées 2022']
    
    for colonne in colonnes_necessaires:
        if colonne not in df.columns:
            raise KeyError(f"La colonne {colonne} est absente du DataFrame.")
    
    # Sélection des variables explicatives et de la cible
    X = df.loc[:, ['écrans', 'fauteuils', 'population de la commune']]
    y = df['entrées 2022']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

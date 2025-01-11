import pandas as pd

def load_data(fichier_path):
    return pd.read_csv(fichier_path, sep=";", encoding="utf-8")

def clean_data(df):
    print("Les valeurs qui manquent :\n", df.isnull().sum())
    df = df.dropna()
    return df

def display_statistics(df):
    stats_columns = ['écrans', 'fauteuils', 'entrées 2021', 'entrées 2022']
    for col in stats_columns:
        if col not in df.columns:
            raise KeyError(f"La colonne {col} n'est pas présente dans le DataFrame.")
    print("Les statistiques descriptives :\n", df[stats_columns].describe())

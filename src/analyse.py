import matplotlib.pyplot as plt
import seaborn as sns

def calculate_mean_entries(df):
    # Cette fonction calcule la moyenne des entrées par fauteuil pour chaque région en 2021 et 2022
    # Elle vérifie également que les colonnes nécessaires sont présentes dans le DataFrame.
    required_columns = ['région administrative', 'entrées 2021', 'entrées 2022', 'fauteuils']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"La colonne {col} n'est pas présente dans le DataFrame.")

    # Création d'une copie pour éviter de modifier les données originales
    df = df.copy()

    # Les Calculs
    df['entrees_2021_par_fauteuil'] = df['entrées 2021'] / df['fauteuils']
    df['entrees_2022_par_fauteuil'] = df['entrées 2022'] / df['fauteuils']
    moyennes_par_region_2021 = df.groupby('région administrative')['entrees_2021_par_fauteuil'].mean()
    moyennes_par_region_2022 = df.groupby('région administrative')['entrees_2022_par_fauteuil'].mean()
    return moyennes_par_region_2021, moyennes_par_region_2022

def plot_top_regions(moyennes_par_region_2021, moyennes_par_region_2022):
    # Affiche un graphique des 10 régions ayant les meilleures entrées moyennes par fauteuil pour les années 2021 et 2022
    # Sélection des 10 meilleures régions pour chaque année
    top_10_regions_2021 = moyennes_par_region_2021.sort_values(ascending=False).head(10)
    top_10_regions_2022 = moyennes_par_region_2022.sort_values(ascending=False).head(10)

    # Création de deux graphiques côte à côte
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Graphique pour 2021
    top_10_regions_2021.plot(kind='bar', color='skyblue', ax=axes[0])
    axes[0].set_title("Les Top 10 des régions - Entrées moyennes par fauteuil en 2021")
    axes[0].set_ylabel("Les entrée moyennes par fauteuil")
    axes[0].set_xlabel("Les régions")
    axes[0].tick_params(axis='x', rotation=45)

    # Graphique pour 2022
    top_10_regions_2022.plot(kind='bar', color='lightcoral', ax=axes[1])
    axes[1].set_title("Les Top 10 des régions - Entrées moyennes par fauteuil en 2022")
    axes[1].set_ylabel("Les entrées moyennes par fauteuil")
    axes[1].set_xlabel("Les régions")
    axes[1].tick_params(axis='x', rotation=45)

    # Espaces
    plt.tight_layout()
    plt.show()

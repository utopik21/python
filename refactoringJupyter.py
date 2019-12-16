import pandas as pd

from pandas import DataFrame

import matplotlib.pyplot as plt

csvFile = 'datas/villes_france.csv'

def get_cities_from_csv(path_file):

  return pd.read_csv(path_file, names=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple', 'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone', 'ville_code_postal', 'ville_commune', 'ville_code_commune', 'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010', 'ville_population_1999', 'ville_population_2012', 'ville_densite_2010', 'ville_surface', 'ville_longitude_deg', 'ville_latitude_deg', 'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms', 'ville_latitude_dms', 'ville_zmin', 'ville_zmax'], header=None, low_memory=False)

def sort_asc_cities_by_population(villes):

  return villes.sort_values(by='ville_population_2012', ascending=False)

def select_50cities(villes_triees):

  return villes_triees.head(50)

def reduce_dataframe(villes):

  return DataFrame(villes, columns=['ville_nom', 'ville_population_2012'])  

def prepare_data_from_csv(csv_path):

  villes = get_cities_from_csv(csv_path)

  return prepare_data(villes)

def prepare_data(villes): 

  villes_triees = sort_asc_cities_by_population(villes)

  villes_50 = select_50cities(villes_triees)

  villes_50_reduced = reduce_dataframe(villes_50)

  return villes_50_reduced

def get_graphe(plotVilles):

  return plotVilles.head(10).plot(x='ville_nom', y='ville_population_2012', kind='barh')

# show_graphe = commande > modifie un etat; ne retourne pas de valeur comme attendu pour une fonction

def show_graphe(plotVilles):

  get_graphe(plotVilles)

  plt.show()
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


def main(file_path):
    city = pd.read_csv(file_path, names=['ville_id', 'ville_departement', 'ville_slug', 'ville_nom', 'ville_nom_simple',
                                         'ville_nom_reel', 'ville_nom_soundex', 'ville_nom_metaphone',
                                         'ville_code_postal', 'ville_commune', 'ville_code_commune',
                                         'ville_arrondissement', 'ville_canton', 'ville_amdi', 'ville_population_2010',
                                         'ville_population_1999', 'ville_population_2012', 'ville_densite_2010',
                                         'ville_surface', 'ville_longitude_de', 'ville_latitude_deg',
                                         'ville_longitude_grd', 'ville_latitude_grd', 'ville_longitude_dms',
                                         'ville_latitude_dms', 'ville_zmin', 'ville_zmax'], header=None,
                       low_memory=False)
    sorted = city.sort_values('ville_population_2012', ascending=False)
    villes_50 = sorted.head(50)
    plotVilles = DataFrame(villes_50, columns=['ville_nom', 'ville_population_2012'])
    plotVilles.head(10).plot(x='ville_nom', y='ville_population_2012', kind='barh')
    return city
from settings import csv
from apps.cities.code import get_cities_from_csv, sort_asc_cities_by_population, select_50cities, reduce_dataframedef test_read_csv():
  villes = get_csv()
  assert villes['ville_nom'].iloc[0]=='OZAN'def get_csv():
  return get_cities_from_csv(csv)def test_sort_asc_cities():
  villes_triees = sort_asc_cities_by_population(get_csv())
  assert villes_triees['ville_nom'].iloc[0] == 'PARIS'def test_select_50cities():
  villes_triees = sort_asc_cities_by_population(get_csv())
  villes_50 = select_50cities(villes_triees)
  assert len(villes_50)== 50def test_dataframe_reduce():
  dataframereduced = reduce_dataframe(get_csv())
  assert list(dataframereduced.columns == ['ville_nom', 'ville_population_2012'])
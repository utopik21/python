
from apps.cities.cities import get_datas_from_cities_csv, sort_column
from settings import CITIES_CSV_FILE
import pandas as pd


def test_get_data_frame_from_csv():
    datas = get_datas_from_cities_csv('../../' + CITIES_CSV_FILE)
    sample = open("golden-master.txt", encoding='utf-8')
    assert datas.head(10).to_string() == sample.read()


def test_sort_column():
    datas = sort_column('../../' + 'datas/villes_france_short.csv', 'Population')
    data_frame = pd.DataFrame(data=datas, index=None)
    assert data_frame.iloc[0]["Villes"] == "Lyon"
    assert data_frame.iloc[1]["Villes"] == "Paris"
    assert data_frame.iloc[2]["Villes"] == "Marseille"

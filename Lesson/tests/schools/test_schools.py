
from apps.schools.schools import get_datas_from_schools_csv, merge_row_by_insee_code
from settings import SCHOOLS_CSV_FILE
import pandas as pd


# def test_get_datas_from_schools_csv():
#     datas = get_datas_from_schools_csv('../../' + SCHOOLS_CSV_FILE)
#     sample = open("golden-master.txt", encoding='utf-8')
#     assert datas.head(10).to_string() == sample.read()


def test_merge_row_by_insee_code():
    data_frame = get_datas_from_schools_csv('../../' + 'datas/lycees_short.csv')
    solution = {'Etablissement': ['', '', ''], 'Ville': ['PARIS', 'LYON', 'MARVEJOLS'], 'Code commune': [75107, 69385, 48092]}
    solution_frame = pd.DataFrame(data=solution, index=None)
    data_frame_grouped = merge_row_by_insee_code(data_frame)
    print(data_frame_grouped)
    print(solution_frame)
    assert data_frame_grouped.iloc[0]["Ville"] == "LYON"
    assert data_frame_grouped.iloc[1]["Ville"] == "MARVEJOLS"
    assert data_frame_grouped.iloc[2]["Ville"] == "PARIS"



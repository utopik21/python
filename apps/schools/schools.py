import pandas as pd

# CRITERES :
# Taux Réussite Attendu France Total séries
# Taux_Mention_attendu_toutes_series


def get_datas_from_schools_csv(file_path):
    data_frame = pd.read_csv(file_path, low_memory=False, sep=';', skipinitialspace=False, usecols=['Code commune','Taux Brut de Réussite Total séries','Taux_Mention_brut_toutes_series'])

    print(data_frame.columns.tolist())
    return data_frame


def merge_row_by_insee_code(data_frame):
    data_frame_grouped = data_frame.groupby(['Code commune']).mean()

    return data_frame_grouped


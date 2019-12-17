import pandas as pd


def get_datas_from_cities_csv(file_path):
    data_frame = pd.read_csv(file_path, low_memory=False, header=None, sep=',', skipinitialspace=False, names=['A' + str(i) for i in range(26)])
    return data_frame


def sort_column(file_path, column):
    data_frame = pd.read_csv(file_path, low_memory=False, header=None, sep=',', skipinitialspace=False, names=['Villes', 'Population'])
    data_frame_sorted = data_frame.sort_values(by=[column], ascending=False)
    return data_frame_sorted

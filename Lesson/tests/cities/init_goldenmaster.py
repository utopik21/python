
from apps.cities.cities import get_data_frame_from_csv
from settings import CITIES_CSV_FILE


def create_golden_master():
    datas = get_data_frame_from_csv('../../' + CITIES_CSV_FILE)
    f = open("golden-master.txt", "w+", encoding='utf-8')
    f.write(datas.head(10).to_string())
    f.close()
    print("File created")


if __name__ == '__main__':
    create_golden_master()

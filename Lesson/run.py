# fonction ‘main’, ce fichier sera exécuté pour lancer l’application
from apps.cities.cities import get_datas_from_cities_csv
from apps.schools.schools import get_datas_from_schools_csv, merge_row_by_insee_code
from settings import CITIES_CSV_FILE
from settings import SCHOOLS_CSV_FILE


def main():
    
    data_frame_schools = get_datas_from_schools_csv(SCHOOLS_CSV_FILE)
    data_frame_schools_merged = merge_row_by_insee_code(data_frame_schools)
    print(data_frame_schools_merged)
    


if __name__ == '__main__':
    main()


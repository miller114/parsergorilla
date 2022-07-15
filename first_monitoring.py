from getting_data import get_products_urls, get_data_from_urls
import time
from cod_to_compare import read_csv, checker_for_new_n_modified
from getting_data import data_log_in
import datetime
import os
import re


def main():
    take_data_today = datetime.datetime.now().strftime("%d_%m")
    file_name = f'monitoring_gorilla_prod{datetime.datetime.now().strftime("%d_%m")}'

    # old = ''.join([file for file in os.listdir('//192.168.1.11/Volume_1/Прайсы/gorilla/') if 'first' in file and 'csv' in file])
    # new = ''.join([file for file in os.listdir('//192.168.1.11/Volume_1/Прайсы/gorilla/') if 'second' in file and 'csv' in file])
    old = ''.join([file for file in os.listdir('C:/Users/mille/Desktop/HW/') if 'first' in file and 'csv' in file])
    new = ''.join([file for file in os.listdir('C:/Users/mille/Desktop/HW/') if 'second' in file and 'csv' in file])

    print(checker_for_new_n_modified(old, new, monitoring_file=file_name))


if __name__ == "__main__":
    main()

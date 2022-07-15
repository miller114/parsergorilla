from getting_data import get_products_urls, get_data_from_urls
import time
from cod_to_compare import read_csv, checker_for_new_n_modified
from getting_data import data_log_in
import datetime
import os

def main():
    count = 1
    while True:
        old_file, new_file = input('Укажите сначала старый файл, затем новый.'
                                   ' Например: "example.csv" "example1.csv"\n>>').split()
        file_path = input('Путь к файлу, если нет пропустите')
        if len(file_path) > 1:
            print(checker_for_new_n_modified(old_file, new_file,
                                             monitoring_file=f'modified_prod({str(count)}'
                                                             f'{datetime.datetime.now().strftime(")%d_%m")}',
                                             path=file_path))
        else:
            print(checker_for_new_n_modified(old_file, new_file,
                                             monitoring_file=f'modified_prod({str(count)}'
                                                             f'{datetime.datetime.now().strftime(")%d_%m")}', path=''))
        count += 1


if __name__ == "__main__":
    main()

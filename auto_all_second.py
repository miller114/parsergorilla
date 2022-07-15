from getting_data import get_products_urls, get_data_from_urls
import time
from cod_to_compare import read_csv, checker_for_new_n_modified
from getting_data import data_log_in
import os
from CONST import FILE_PATH_PARS, FILE_PATH_MONITORING
import datetime


def main():
    global timer
    count = 1

    take_data_today = datetime.datetime.now().strftime("%d_%m")
    names_files = f'second_gorilla_prod_data'

    print(get_products_urls(names_files, choice=['all_from_site']))
    print(get_data_from_urls(names_files))


if __name__ == "__main__":
    main()

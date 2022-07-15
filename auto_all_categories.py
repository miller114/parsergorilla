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
    data_list = []
    while True:
        take_data_today = datetime.datetime.now().strftime(")%d_%m")
        names_files = f'gorilla_prod_data({str(count)}{take_data_today}'
        data_list.append(take_data_today)
        if count == 1:
            timer = input('Введите через какой интервал будет работать парссер(в часах)\n>>')
            # path = os.path.join("C:/Users/mille/Desktop/HW")
            # file_name = os.path.join(input("Укажите полный путь к файлу и название для файла "
            #                                "в формате 'C:/Users/Desktop/filename'\n>>"))
        print(get_products_urls(names_files, choice=['all_from_site']))
        print(get_data_from_urls(names_files))
        if count >= 2:
            old_file = f"gorilla_prod_data({str(count - 1)}{data_list[count-2]}.csv"
            new_file = f"gorilla_prod_data({str(count)}{take_data_today}.csv"
            monitoring_file_name = f'monitoring({str(count - 1)}{take_data_today}.csv'
            print(checker_for_new_n_modified(old_file, new_file, monitoring_file_name))
        time.sleep(float(timer) * 3600)
        count += 1
        # except Exception as e:
        #     print(e)


if __name__ == "__main__":
    main()

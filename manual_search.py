from getting_data import get_products_urls, get_data_from_urls
import time
from cod_to_compare import read_csv, checker_for_new_n_modified
from getting_data import data_log_in
import os
import datetime


def main():
    global file_name
    global file_path
    count = 1
    while True:
        data_list = []
        take_data_today = datetime.datetime.now().strftime(")%d_%m")
        # names_files = f'gorilla_prod_data({str(count)}{take_data_today}'
        data_list.append(take_data_today)
        try:
            if count == 1:
                # data_log_in.update({'username': input('login'), 'passwd': input('password')})
                file_path, file_name = (input("Укажите полный путь к файлу и название для файла "
                                              "в формате(разделить путь название знаком вопроса)"
                                              " 'C:/Users/Desktop/?file_name'\n>>")).split('?')
            print(get_products_urls(f"{file_name}({str(count)}{take_data_today}",
                                    path=file_path))
            print(get_data_from_urls(f"{file_name}({str(count)}{take_data_today}",
                                     path=file_path))
            count += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

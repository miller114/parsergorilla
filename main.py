from getting_data import get_products_urls, get_data_from_urls
import time
from cod_to_compare import read_csv, checker_for_new_n_modified
from getting_data import data_log_in


def main():
    count = 0
    while True:
        if count == 0:
            data_log_in.update({'username': input('login'), 'passwd': input('password')})
        timer = input('Введите через сколько надо проверить(в часах)\n>>')
        time.sleep(float(timer) * 3600)
        file_name = input("Впишите название файла для сбора ссылок и парссинга данных\n>>")
        print(get_products_urls(file_name))
        get_data_from_urls(file_name)
        ask_to_compare = input('Нужно сравнивать файлы?(y/n)\n >>')
        if ask_to_compare == 'y':
            old_file, new_file = input('Укажите сначала старый файл, затем новый.'
                                       ' Например: "example.csv" "example1.csv"\n>>').split()
            checker_for_new_n_modified(old_file, new_file)
        count += 1


if __name__ == "__main__":
    main()

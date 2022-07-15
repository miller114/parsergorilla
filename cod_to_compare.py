import csv
import itertools
import os
from CONST import FILE_PATH_PARS, FILE_PATH_MONITORING

def read_csv(file_name, file_path=FILE_PATH_PARS):
    result = []
    with open(file_path + file_name, encoding='utf8') as f1:
        reader = csv.reader(f1)
        for row in reader:
            result.append(row)
    return result


def checker_for_new_n_modified(old_file, new_file, monitoring_file, path=FILE_PATH_MONITORING):
    old = read_csv(old_file)
    new = read_csv(new_file)
    lst_new_pr = []
    lst_modified_pr = []
    temp = set()
    temp1 = set()
    new_: str
    old_: str
    for old_, new_ in itertools.product(old, new):
        count = 0

        if new_ not in old:
            if new_[6] == old_[6]:
                lst_modified_pr.append({
                    'OLD': old_, 'NEW': new_
                })
        temp1.add(old_[6])
        temp.add(new_[6])

    attr_id_prod = temp - temp1
    for products in new:
        for id_prod in attr_id_prod:
            if id_prod == products[6]:
                lst_new_pr.append(products)

    if len(lst_new_pr) > 0 or len(lst_modified_pr) > 0:
        with open(f'{path}{monitoring_file}.csv', 'w', encoding='utf8') as file:
            fieldnames = ['Название', 'Ссылка', 'Цена', 'Старая цена', 'Наличие', 'Код товара', 'Ид', 'Размер',
                          'Изменения']
            w = csv.DictWriter(file, fieldnames=fieldnames)
            w.writeheader()
            for fields in range(len(lst_modified_pr)):
                ch = 0
                str_attr = ''
                # for i in ('OLD', 'NEW'):
                ch += 1
                if str(lst_modified_pr[fields].get('OLD')[0]) != str(lst_modified_pr[fields].get('NEW')[0]) and \
                        ch == 1:
                    str_attr += 'Название'
                if str(lst_modified_pr[fields].get('OLD')[1]) != str(lst_modified_pr[fields].get('NEW')[1]) and \
                        ch == 1:
                    str_attr += 'Ссылка'
                if str(lst_modified_pr[fields].get('OLD')[2]) != str(lst_modified_pr[fields].get('NEW')[2]) and \
                        ch == 1:
                    str_attr += 'Цена'
                if str(lst_modified_pr[fields].get('OLD')[3]) != str(lst_modified_pr[fields].get('NEW')[3]) and \
                        ch == 1:
                    str_attr += 'Старая цена'
                if str(lst_modified_pr[fields].get('OLD')[4]) != str(lst_modified_pr[fields].get('NEW')[4]) and \
                        ch == 1:
                    str_attr += 'Наличие'
                if str(lst_modified_pr[fields].get('OLD')[5]) != str(lst_modified_pr[fields].get('NEW')[5]) and \
                        ch == 1:
                    str_attr += 'Код товара'
                if str(lst_modified_pr[fields].get('OLD')[6]) != str(lst_modified_pr[fields].get('NEW')[6]) and \
                        ch == 1:
                    str_attr += 'Ид'
                if str(lst_modified_pr[fields].get('OLD')[7]) != str(lst_modified_pr[fields].get('NEW')[7]) and \
                        ch == 1:
                    str_attr += 'Размер'
                w.writerow({'Название': lst_modified_pr[fields].get('NEW')[0],
                            'Ссылка': lst_modified_pr[fields].get('NEW')[1],
                            'Цена': lst_modified_pr[fields].get('NEW')[2],
                            'Старая цена': lst_modified_pr[fields].get('NEW')[3],
                            'Наличие': lst_modified_pr[fields].get('NEW')[4],
                            'Код товара': lst_modified_pr[fields].get('NEW')[5],
                            'Ид': lst_modified_pr[fields].get('NEW')[6],
                            'Размер': lst_modified_pr[fields].get('NEW')[7],
                            'Изменения': str_attr,
                            }
                           )
                # w.writerow({'Название': '',
                #             'Ссылка': '',
                #             'Цена': '',
                #             'Старая цена': '',
                #             'Наличие': '',
                #             'Код товара': '',
                #             'Ид': '',
                #             'Размер': '',
                #             'Изменения': ''})
            w.writeheader()
            for data in lst_new_pr:
                w.writerow({'Название': data[0],
                            'Ссылка': data[1],
                            'Цена': data[2],
                            'Старая цена': data[3],
                            'Наличие': data[4],
                            'Код товара': data[5],
                            'Ид': data[6],
                            'Размер': data[7],
                            'Изменения': 'Новые товары'})

        return f'Файл {monitoring_file} создан в {path}'
    else:
        return f'Изменений не найдено'



if __name__ == '__main__':
    print(checker_for_new_n_modified(old_file='first_gorilla_prod_data.csv', new_file='testmanual_men_fut_majki.csv', monitoring_file='monitoring_test_file'))

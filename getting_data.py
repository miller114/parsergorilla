import csv
import random
import time

from pars_js import get_attr, get_attr1, get_attr_id
import requests
from bs4 import BeautifulSoup
from CONST import *


s = requests.Session()
response_login = s.post(link, data=data_log_in, headers=headers).text


def get_products_urls(file_name, choice=None, path=FILE_PATH_PARS):
    if choice is None:
        choice = input('Впишите категорию, например :"Мужчинам"(указываем через пробел),'
                       ' "all"(для всех) или ссылки(через пробел)\n>>').split()

    jshop_temp_list = []
    jshop_temp_list_id = []
    for_me = []
    # choice = input('Впишите категорию например "Мужчинам" или "all" для всех').split()
    if choice == ['all']:
        try:
            # Проходимся по категориям
            for ch in group_urls.items():
                # Выборка, считываем сразу
                if ch[0] != 'Мужчинам' and ch[0] != 'Женщинам' and ch[0] != 'Аксессуары':
                    response = s.get(url=ch[1], headers=headers)
                    soup = BeautifulSoup(response.text, 'lxml')
                    product = soup.find('div', class_='jshop list_product uk-margin-large-bottom'). \
                        find_all('div', class_='block_product')

                    for i in product:
                        if f"https://gorillawear.ua{i.find('a').get('href')}" in jshop_temp_list:
                            continue
                        if get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}") in jshop_temp_list_id:
                            continue
                        else:
                            jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                            jshop_temp_list_id.append(get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}"))
                    time.sleep(random.randrange(1, 3))
                    print(f'Выполнено сбор ссылок в разделе {ch[0]}')

                else:
                    # остальное переходим в подкатегории
                    counter = 0
                    response = s.get(url=ch[1], headers=headers)
                    soup = BeautifulSoup(response.text, 'lxml')

                    jshop_list_category = soup.find('div', class_='uk-width-expand@l uk-margin-bottom'). \
                        find('div', class_='jshop_list_category').find_all('div', class_='row-fluid')

                    for group_of_product in jshop_list_category:
                        group_of_product = f'https://gorillawear.ua{group_of_product.find("a").get("href")}'

                        counter += 1

                        response = s.get(url=group_of_product, headers=headers)
                        soup = BeautifulSoup(response.text, 'lxml')

                        product = soup.find('div', class_='jshop list_product uk-margin-large-bottom'). \
                            find_all('div', class_='block_product')

                        for i in product:
                            if f"https://gorillawear.ua{i.find('a').get('href')}" in jshop_temp_list:
                                continue
                            if len(get_attr(f"https://gorillawear.ua{i.find('a').get('href')}")) == 0:
                                jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                            elif get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}") in jshop_temp_list_id:
                                continue

                            else:
                                jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                                jshop_temp_list_id.append(
                                    get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}"))
                        time.sleep(random.randrange(1, 3))

                        # информативный принт

                        # print(f'Выполнено {counter} c {len(jshop_list_category)} в разделе {ch[0]}')
                    time.sleep(random.randrange(1, 3))

        except Exception as e:
            print(e)
    elif choice[0].startswith('http'):
        try:
            # Проходимся по ссылкам
            for ch in choice[0].split():
                response = s.get(url=ch, headers=headers)
                soup = BeautifulSoup(response.text, 'lxml')
                product = soup.find('div', class_='jshop list_product uk-margin-large-bottom'). \
                    find_all('div', class_='block_product')

                for i in product:
                    if f"https://gorillawear.ua{i.find('a').get('href')}" in jshop_temp_list:
                        continue
                    if len(get_attr(f"https://gorillawear.ua{i.find('a').get('href')}")) == 0:
                        jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                    elif get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}") in jshop_temp_list_id:
                        continue

                    else:
                        jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                        jshop_temp_list_id.append(get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}"))
                time.sleep(random.randrange(1, 3))

                # информативный принт
                # print(f'Выполнено сбор ссылок в {ch}')

        except Exception as e:
            print(e)

    elif choice == ['all_from_site']:
        try:
            temp_f_main_links = []
            response = s.get(url='https://gorillawear.ua/muzhchinam/futbolki', headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            links = soup.find('div', class_='moduletable_menu uk-visible@l').find_all('a')
            for i in links:
                temp_f_main_links.append(f"https://gorillawear.ua{i.get('href')}")

            for link in temp_f_main_links:
                response = s.get(url=link, headers=headers)
                soup = BeautifulSoup(response.text, 'lxml')
                try:
                    product = soup.find('div', class_='jshop list_product uk-margin-large-bottom'). \
                        find_all('div', class_='block_product')
                except:
                    continue
                for i in product:
                    if f"https://gorillawear.ua{i.find('a').get('href')}" in jshop_temp_list:
                        continue
                    if len(get_attr(f"https://gorillawear.ua{i.find('a').get('href')}")) == 0:
                        jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                    elif get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}") in jshop_temp_list_id:
                        continue

                    else:
                        jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                        jshop_temp_list_id.append(get_attr_id(f"https://gorillawear.ua{i.find('a').get('href')}"))
                time.sleep(random.randrange(1, 3))

                # информативный принт
                print(f'Выполнено сбор ссылок в {link}')
        except Exception as e:
            print(e, link)

    else:
        try:
            # Проходимся по категориям
            for ch in choice:
                # Выборка, считываем сразу
                if ch != 'Мужчинам' and ch != 'Женщинам':
                    response = s.get(url=group_urls.get(ch), headers=headers)
                    soup = BeautifulSoup(response.text, 'lxml')
                    product = soup.find('div', class_='jshop list_product uk-margin-large-bottom'). \
                        find_all('div', class_='block_product')
                    print(f'Выполнено сбор ссылок в разделе {ch[0]}')

                    for i in product:
                        if f"https://gorillawear.ua{i.find('a').get('href')}" in jshop_temp_list:
                            continue
                        else:
                            jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")
                else:
                    # остальное переходим в подкатегории
                    counter = 0
                    response = s.get(url=group_urls.get(ch), headers=headers)
                    soup = BeautifulSoup(response.text, 'lxml')

                    jshop_list_category = soup.find('div', class_='uk-width-expand@l uk-margin-bottom'). \
                        find('div', class_='jshop_list_category').find_all('div', class_='row-fluid')

                    # todo тут в можно поставить выбор подкатегории
                    for group_of_product in jshop_list_category:
                        group_of_product = f'https://gorillawear.ua{group_of_product.find("a").get("href")}'

                        counter += 1

                        response = s.get(url=group_of_product, headers=headers)
                        soup = BeautifulSoup(response.text, 'lxml')

                        product = soup.find('div', class_='jshop list_product uk-margin-large-bottom'). \
                            find_all('div', class_='block_product')

                        for i in product:
                            if f"https://gorillawear.ua{i.find('a').get('href')}" in jshop_temp_list:
                                continue
                            else:
                                jshop_temp_list.append(f"https://gorillawear.ua{i.find('a').get('href')}")

                        print(f'Выполнено {counter} c {len(jshop_list_category)} в разделе {ch}')
                    time.sleep(random.randrange(2, 5))

        except Exception as e:
            print(e)
    # with open('my.txt', 'w', encoding='utf8') as f:
    #     for i in for_me:
    #         f.write(f"{str(i)}\n")

    # записываем ссылки на продукты
    try:
        with open(f'{path}{file_name}urls.txt', 'w', encoding='utf8') as file:
            for jshop in enumerate(jshop_temp_list):
                file.write(f'{jshop[0] + 1} {jshop[1]}\n')
    except Exception as e:
        print(e)
    return f'Работа по сбору ссылку закончена, в категориях/ссылкам: {", ".join([i for i in choice])} '


def get_text(el) -> str:
    if not el:
        return ""
    return el.text


def get_all(el) -> str:
    return el.find_all() if el else ""


def get_data_from_urls(file_name, path=FILE_PATH_PARS):
    with open(f'{path}{file_name}urls.txt') as file:
        urls_list = [line.strip().split()[1] for line in file.readlines()]

    urls_count = len(urls_list)
    temp = []
    temp_id = []
    pr_data = []
    try:

        for url in enumerate(urls_list):
            response = s.get(url=url[1], headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            product_url = url[1]
            product_name = get_text(soup.find('div', class_='span8 jshop_img_description').find('h1'))
            product_price = get_text(soup.find('div', class_='prod_price uk-margin-bottom')).strip().replace('\r\n',
                                                                                                             ''). \
                replace(' ', '')
            product_in_stock = get_text(soup.find('div', class_='qty_in_stock uk-margin-bottom'))
            product_code = get_text(
                soup.find('div', class_='span8 jshop_img_description').find('span', class_='uk-text-meta'))
            # product_id = None

            time.sleep(random.randrange(2, 3))

            chars = get_attr(product_url)
            if len(chars) == 0:
                if product_name in temp:
                    continue
                else:
                    pr_data.append(
                        {
                            'Название': product_name,
                            'Ссылка': product_url,
                            'Цена': product_price.split('грн')[0],
                            'Старая цена': product_price.split('грн')[1] if len(product_price.split('грн')[1]) != 0
                            else 0,
                            'Наличие': 1,
                            'Код товара': product_code.split(':')[1],
                            'Ид': product_name,
                            'Размер': '',
                        }
                    )
                    temp.append(product_name)
            else:
                for attrib in range(len(chars)):
                    if chars[attrib].get('Уникальный номер') in temp_id:
                        continue
                    else:
                        pr_data.append(
                            {
                                'Название': product_name,
                                'Ссылка': product_url,
                                'Цена': chars[attrib].get('Цена') if len(chars[attrib].get('Цена')) > 0
                                                                     and chars[attrib].get(
                                    'Цена') != '0' else product_price,
                                'Старая цена': chars[attrib].get('Старая цена'),
                                'Наличие': chars[attrib].get('Наличие') if len(chars[attrib].get('Наличие')) > 0
                                else product_in_stock,
                                'Код товара': product_code.split(':')[1],
                                'Ид': chars[attrib].get('Уникальный номер') if len(
                                    chars[attrib].get('Уникальный номер')) > 0
                                else '',
                                'Размер': chars[attrib].get('Размер') if len(chars[attrib].get('Размер')) > 0
                                else '',
                            }
                        )
                        temp_id.append(chars[attrib].get('Уникальный номер'))
            print(f'Отработала ссылка:{url[1]}  {url[0] + 1}')
            # Запись в csv
        with open(f'{path}{file_name}.csv', mode='w', newline='', encoding='utf8') as product_date:
            fieldnames = ['Название', 'Ссылка', 'Цена', 'Старая цена', 'Наличие', 'Код товара', 'Ид', 'Размер']
            product_date_writer = csv.DictWriter(product_date, fieldnames=fieldnames)
            product_date_writer.writeheader()
            name_check = ''
            counter = 1
            for pr in pr_data:
                if pr.get('Название') != name_check:
                    product_date_writer.writerow({'Название': '', 'Ссылка': '',
                                                  'Цена': '', 'Старая цена': '',
                                                  'Наличие': '', 'Код товара': '',
                                                  'Ид': '', 'Размер': ''})
                product_date_writer.writerow({'Название': pr.get('Название'), 'Ссылка': pr.get('Ссылка'),
                                              'Цена': pr.get('Цена'), 'Старая цена': pr.get('Старая цена'),
                                              'Наличие': pr.get('Наличие'), 'Код товара': pr.get('Код товара'),
                                              'Ид': pr.get('Ид'), 'Размер': pr.get('Размер')})
                name_check = pr.get('Название')

    except Exception as ex:
        print(ex)
    return f"{file_name} Успешно создан в {path}"


# if __name__ == '__main__':
#     print(get_products_urls('testmanual_men_fut_majki', choice=['https://gorillawear.ua/muzhchinam/futbolki https://gorillawear.ua/muzhchinam/majki']))
#     print(get_data_from_urls('testmanual_men_fut_majki'))

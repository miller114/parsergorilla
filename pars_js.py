import requests


def get_attr(url):
    response = requests.post(url)
    attr_list = []
    for i in response.text.split():
        if i == 'xhr.open("POST",':
            se = requests.get(
                f'https://gorillawear.ua{response.text.split()[response.text.split().index(i) + 1][1:-2]}')

            for _ in range(len(se.json().get('data')[0])):
                # if float(se.json().get('data')[0][_].get('count')) > 0:

                attr_list.append({'Размер': se.json().get('data')[0][_].get('name_ru'),
                                  'Уникальный номер': se.json().get('data')[0][_].get('product_attr_id'),
                                  'Цена': se.json().get('data')[0][_].get('price').split('.')[0],
                                  'Старая цена': se.json().get('data')[0][_].get('old_price').split('.')[0],
                                  'Наличие': '1' if se.json().get('data')[0][_].get('count').split('.')[0] != "0"
                                  else se.json().get('data')[0][_].get('count').split('.')[0],
                                  })

    return attr_list


# if __name__ == '__main__':
#     print(
#         get_attr(url='https://gorillawear.ua/zhenshchinam/topy/top-neiro-seamless-sports-bra-purple')[1].get('Наличие'))

def get_attr1(url):
    response = requests.post(url)
    attr_list = []
    for i in response.text.split():
        if i == 'xhr.open("POST",':
            se = requests.get(
                f'https://gorillawear.ua{response.text.split()[response.text.split().index(i) + 1][1:-2]}')
            attr_id = (se.url.split('=')[-1])

    return attr_id


# print(get_attr1('https://gorillawear.ua/muzhchinam/majki/futbolka-dakota-sleeveless-t-shirt-black'))

def get_attr_id(url):
    response = requests.post(url)
    attr_list = []
    tmp = []
    for i in response.text.split():
        if i == 'xhr.open("POST",':
            se = requests.get(
                f'https://gorillawear.ua{response.text.split()[response.text.split().index(i) + 1][1:-2]}')

            for _ in range(len(se.json().get('data')[0])):
                # if float(se.json().get('data')[0][_].get('count')) > 0:
                attr_list.append(se.json().get('data')[0][_].get('product_attr_id'))

    return attr_list




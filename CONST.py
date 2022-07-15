import fake_useragent
import os
user = fake_useragent.UserAgent().random

# FILE_PATH_PARS = os.path.join('//192.168.1.11/Volume_1/Прайсы/gorilla/')
FILE_PATH_PARS = os.path.join('C:/Users/mille/Desktop/HW/')
FILE_PATH_MONITORING = os.path.join('C:/Users/mille/Desktop/HW/')
# FILE_PATH_MONITORING = os.path.join('//192.168.1.11/Volume_1/Прайсы/')

link = 'https://gorillawear.ua/component/jshopping/user/loginsave?Itemid=0'

data_log_in = {
    'username': "",
    # 'username': "sup@foods-body.ua",
    # 'passwd': "qwerty56",
    'passwd': "",
    'return': "1",
    '': "1"
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "user-agent": str(user),
}

group_urls = {
    'Мужчинам': 'https://gorillawear.ua/muzhchinam',
    'Женщинам': 'https://gorillawear.ua/zhenshchinam',
    'Обувь': 'https://gorillawear.ua/obuv',
    'Аксессуары': 'https://gorillawear.ua/aksessuary',
    'Акции': 'https://gorillawear.ua/aktsii'

}
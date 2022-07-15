import re
import time

from bs4 import BeautifulSoup
import requests
import fake_useragent

session = requests.Session()
link = 'https://gorillawear.ua/component/users/?task=user.login&Itemid=101'
link1 = 'https://gorillawear.ua/component/jshopping/user/loginsave?Itemid=0'
user = fake_useragent.UserAgent().random

header = {'user-agent': user}

def get_token():
    response = session.post(link, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")

    token = response.text.split()
    tok = soup.find_all('input', {'type': 'hidden'})[-1].get('name')
    val = soup.find_all('input', {'type': 'hidden'})[-1].get('value')
    tok_nd_value = {
        'token': str(tok),
        'value': str(val),
    }
    return tok_nd_value

tok = get_token().get('token')
val = get_token().get('value')
data = {
    'username':	"*****",
    'passwd': "******",
    'return': '1',
    str(tok): str(val)
}

# response = session.post(link, data=data, headers=header)



resp = session.post(link1, headers=header, data=data)
time.sleep(2)
print(resp.content)
with open('my.html', 'w', encoding="utf8") as f:
    f.write(resp.text)
print(tok)
print(val)

# profile = 'https://gorillawear.ua/menyu-polzovatelya/lichnyj-kabinet'
#
# profile_response = session.get(profile, headers=header)
# cookies_dict = [
#     {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
#     for key in session.cookies
# ]





# import requests
# from bs4 import BeautifulSoup
# import time
# headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
#
# data = {'authenticity_token':'',
#     'email':'', # Email
#     'password':''  # Пароль
#     }
#
# url = 'https://www.strava.com/session'
#
# session = requests.Session() # Сессия
#
# def get_token():# Метод, для получения токена
#   response = session.post(url,headers=headers)
#   soup = BeautifulSoup(response.text,"html.parser")
#   token = soup.find('input',{'name':'authenticity_token'}).get('value')
#   return token # Возвращает токен
#
#
# def auth(): # Метод, для авторизации
#   response = session.post(url,headers=headers,data=data)
#   return response.text
#
# data['authenticity_token'] = get_token() # Вызывает метод для получения токена, и результат заносим в словарь
#
# time.sleep(2) # Пауза 2 сек :)
# html = auth() # Авторизируемся. В html будет наш ответ после авторизации
#
# if 'Log Out' in html: # Если строка 'Log Out' есть в html, значит авторизация прошла успешно
#   print('Login OK!')
# else:
#   print('Login Error!')
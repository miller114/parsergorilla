import re


def get_cod_from_str(text: str):
    split_text = re.split('[ /]', text)
    symbols = {
        "Aa": 1, "Аа": 27, "Щщ": 53,
        "Bb": 2, "Бб": 28, "Ъъ": 54,
        "Cc": 3, "Вв": 29, "Ыы": 55,
        "Dd": 4, "Гг": 30, "Ьь": 56,
        "Ee": 5, "Дд": 31, "Ээ": 57,
        "Ff": 6, "Ее": 32, "Юю": 58,
        "Gg": 7, "Ёё": 33, "Яя": 59,
        "Hh": 8, "Жж": 34,
        "Ii": 9, "Зз": 35,
        "Jj": 10, "Ии": 36,
        "Kk": 11, "Йй": 37,
        "Ll": 12, "Кк": 38,
        "Mm": 13, "Лл": 39,
        "Nn": 14, "Мм": 40,
        "Oo": 15, "Нн": 41,
        "Pp": 16, "Оо": 42,
        "Qq": 17, "Пп": 43,
        "Rr": 18, "Рр": 44,
        "Ss": 19,  "Сс": 45,
        "Tt": 20, "Тт": 46,
        "Uu": 21, "Уу": 47,
        "Vv": 22, "Фф": 48,
        "Ww": 23, "Хх": 49,
        "Xx": 24, "Цц": 50,
        "Yy": 25, "Чч": 51,
        "Zz": 26, "Шш": 52,
    }
    text_number = ''
    for item in split_text:
        for value, key in symbols.items():
            if item[0] in value:
                # print(f"{item}={key}")
                text_number += str(key)
    return int(text_number)


# print(get_cod_from_str('Бейсболка Trucker Cap Black/Red'))
# print(get_cod_from_str('Шапка Oxford Beanie Black'))

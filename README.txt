1. Для работы надо установить пакеты из файла requirements. Командой pip3 install -r requirements.txt
2. Запуск производится из файла main
3. В файле compare идет сравнение между двумя файлами csv. Создаются 2 файла, в одном добавляются те продукты
которых не было, а во втором модифицированные(частично измененные)

Есть 3 варианта парссинга, по готовым категориям('Мужчинам', 'Женщинам', 'Обувь', 'Аксессуары', 'Акции'),
по ссылкам и по всем категориям командой('all').

Таймер задается в часах.

В файле getting_data. 14, 15 строчка кода, впишите ваш логин, пароль 'username': "example_login",
                                                                       'passwd': "test_pass",

Добавлены файлы: auto_all_categories.py, manual_search.py, comparing.py.

В файле auto_all_categories.py, стоят настройки на все категории и задается интервал, через который производится
сбор данных. Файлы создаются каждый раз с названием(которое задается 1 раз) и дальнейшим прибавлением числа повторов.

В файле manual_search.py, нужно указывать каждый раз ссылку, категорию. Можно добавлять 2 и более ссылок, категорий
подряд. Так же как и в автоматическом режиме название файла меняется автоматически.

В файле comparing.py, сравниваем изменения между 2 файлами.

Если вызываете через cmd. Заходите в рабочую папку парссера и соответственно указываете название файла с приставкой .py


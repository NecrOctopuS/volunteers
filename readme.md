# База волонтеров

Flask REST.
База волонтеров с поиском по району и улице, а также отправка заявки на помощь.

## Запуск

Для запуска сайта у вас уже должен быть установлен Python 3.

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите команды для базы данных
```
flask db upgrade
python3 add_data.py
```
- Запустите сервер командой `flask run`

После этого переходите по ссылке [127.0.0.1:5000](http://127.0.0.1:5000), вы увидите главную страницу.

Либо задеплойте его на [Heroku](https://heroku.com/).

В файле `.env` или в настройках окружения создайте следующие переменные:
```
SECRET_KEY='my-super-secret-phrase-I-dont-tell-this-to-nobody' #Секретный ключ проекта
```


## Особенности

Изначальные данные находятся в файлах
```
districts.json
streets.json
volunteers.json
```
Их можно записать в базу данных запустив скрипт командой `python3 add_data.py`.

## Цели проекта

Код написан в учебных целях — это проектное задание первой недели в курсе по Flask REST на сайте [Stepik](https://stepik.org/).
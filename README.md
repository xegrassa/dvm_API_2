# Сокращение URL

Консольное приложение для сокращение URL с помощью сервиса [Bitly](https://bitly.com/). (**Проект учебный**)

## Установка

Клонируйте проект и установите зависимости командами ниже.

```
git clone https://github.com/xegrassa/dvm_API_2.git
cd dvm_API_2
pip install -r requirements.txt
```

Для работы в корне проекта создайте файл **.env**
```
BITLY_TOKEN = Ваш_токен_от_аккаунта_bitly
```

## Получение ТОКЕНА
- Получить токен можно зарегистрировавшись на сайте [bitly.com](https://bitly.com/). 
- После надо перейти в **Developer settings** в настройках аккаунта или перейдя по ссылке [bitly.com/settings/api](https://app.bitly.com/settings/api/)
- Нажать на **Generate token**

![img](https://user-images.githubusercontent.com/52129535/159123036-60ab0a6e-1b93-4077-98f7-7028c42bd3d6.jpg)

## Запуск

Мини справку о работе можно вызвать через опцию **-h**. `python main.py -h`

Находясь в корне проекта запустите проект с переданным URL или Bitlink
- url - https://google.com 
- bitlink - [https://bit.ly/34y5mhm](https://bit.ly/34y5mhm)
```
python main.py http://google.com
```

**Пример работы:**
[![asciicast](https://asciinema.org/a/475885.svg)](https://asciinema.org/a/475885)


## Зависимости

* [Python 3.10](https://www.python.org/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
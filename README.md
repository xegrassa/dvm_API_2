# Сокращение URL

Консольное приложение для сокращение URL с помощью сервиса Bitly. (**Проект учебный**)

### Установка

Клонируйте проект и установите зависимости командами ниже.

```
git clone https://github.com/xegrassa/dvm_API_2.git
cd dvm_API_2
pip install -r requirements.txt
```
***
Для работы в корне проекта создайте файл **.env**
```
TOKEN = Ваш_токен_от_аккаунта_bitly
```

### Запуск

Мини справку о работе можно вызвать через опцию **-h**. `python main.py -h`
***
Находясь в корне проекта запустите проект с переданным URL или Bitlink
- url - http://google.com 
- bitlink - bit.ly/34y5mhm
```
python main.py http://google.com
```




## Зависимости

* [Python 3.10](https://www.python.org/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
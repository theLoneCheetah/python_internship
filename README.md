# Создание простого веб-сервера на Django

Файл для создания бегущей строки хранится по newsite/video/running_string.py. Его можно запустить и без создания веб-сервера, он выдаст файл с некоторой бегущей строкой для примера.

Для запуска веб-сервера необходимо настроить окружение Python на своём локальном устройстве и скачать данные проекта каталога newsite/.

В приложении video (каталог newsite/video/) предусмотрен ввод в адресной строке <host:port>/gettext и <host:port>/gettext/?text=<str>, последняя команда приведёт в исполнение скрипт создания бегущей строки на основе введённого адреса, который сохранится в Загрузки (Downloads) на вашем устройстве. В файле views.py настроен обработчик, запускающий для этого скрипт running_string.py, в файле models.py - модель для базы данных, а в файле middleware.py - перехватчик запросов, добавляющий записи обо всех поступивших к серверу запросах в базу.

Помимо этого, вы сможете найти файл базы данных после выполнения нескольких запросов и пример видеофайла с бегущей строкой в каталоге newsite/.

Скрипт с бегущей строкой в [Google Colab](https://colab.research.google.com/drive/1-pj5-MJg6ArBEfI6db9Hc7vmjEuOvLv7?usp=sharing).

Ниже приведена ссылка на Colab, в котором клонируется данный репозиторий, создаётся локальное окружение и с помощью токена ngrok развёртывается веб-сервер с запросами вида:
```
https://<ваш_домен>.ngrok-free.app/gettext/?text=<str>
```

[Colab для запуска](https://colab.research.google.com/drive/1OdFF_TvSQtelLh9Vek2LlTC7H28AGnQr?usp=sharing)

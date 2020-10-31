# PY3-Advanced-Telegram-Bot
#### by Advanced Develope

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

**Py3-Avanced-Telegram-Bot** - это обучаемый Telegram-бот, написанный командой Advanced Develope.

Вот несколько его особенностей:

  - Работает на технологии Websocket.
  - Возможно обучить различным разговорным скриптам.
  - Открытый и понятный исходный код.

### Премущества использования бота

  - Способен работать 24/7
  - Отсутствует человеческий фактор
  - Не требует каких-либо финансовых вложений

Подойдет всем компаниям, где необходима работа с клиентами (консалтинг, информирование, продажи и т.д.).

### Настройка и установка

Данный бот написан на Python 3.7 и способен работать как на локальном, так и на удаленном сервере.
В данном репозитории присутствует файл конфигурации **main.yml.txt**, который позволяет в автоматическом режиме используя **Github Actions**, загружать и запускать бота на **Heroku** (нужно удалить из имени файла конфигурации *.txt*).

##### .env
-- Настройка переменных окружения
```sh
BOT_API_TOKEN="Токен Telegram-бота"
BOT_WELCOME_PIC="Ссылка на изображение"
HEROKU_APP_URL="URL-адрес приложения на Heroku"
WEBSITE_URL="Ссылка на сайт вашего проекта"
```

#### config.py
-- Файл конфигурации
```sh
path = 'pyBot_dict.json' # Словарь
lvl = 0.7 # Коэффициент сравнения сообщений с записями в словаре
```

#### pyBot_dict.json
-- Словарь бота
```json
{
    "q": "Как купить вашу продукцию?",
    "a": "Можете оформить заказ на нашем сайте!",
    "x": "website_kbd"
}
```

**q** - Сообщение, получаемое ботом
**a** - Сообщение, которым ответит бот
**x** - Тип отображаемой клавиатуры для пользователя

Бот находит наиболее подходящий ответ исходя из выставленного коэффициента сравнения входящих сообщений с существующими записями в словаре. В случае, когда бот не находит подходящую запись, в ответ отправляет "...".

### Обучение бота

Для запуска процесса обучения бота выполните скрипт:

```sh
$ python3 learnBot.py
```

### Расширенная версия*

 - Логические цепочки диалогов
 - Уведомления по e-mail / в личные сообщения / в канал Telegram
 - Прием платежей

И другие возможности, отсутствующие в текущей версии.

Тип лицензии
----

MIT


*Расширенная версия распространяется под другой лицензией и на платной основе.*
*Подробности уточняйте по E-mail: advanced.develope@gmail.com*

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

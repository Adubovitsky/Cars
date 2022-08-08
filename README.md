# Cars
По предварительному плану данный проект будет собирать информацию с сайтов объявлений о продаже машин в России и в Европе, чтобы сравнивать цены по разным моделям и находить наиболее интересные модели, которые будет выгодно купить за рубежом и затем продать в России.
На текущий момент сделан первый шаг. Подключен парсер по сайту авто.ру, который загружает в базу данных следующую информацию: марка, модель, год выпуска, пробег, цена, объем двигателя. Также в модели данных заведены таблицы Age и Mileage, с помощью которых можно будет в дальнейшем фильтровать данные по группам по возрасту и пробегу автомобилей
По условиям домашнего задания база данных включена в файл gitignore. Чтобы проверить работу сайта, необходимо сначала запустить команду «age», c помощью которой загрузятся справочники Age и Mileage и затем запустить команду «filldb», которая загружает данные с сайта авто.ру. По умолчанию сейчас загружаются данные по марке «Subaru». Марку автомобиля можно поменять в стр.111 кода в файле filldb.py
Просмотр списка обьявлений можно по команде "getdb"

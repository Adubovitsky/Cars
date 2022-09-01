# Cars
По предварительному плану данный проект будет собирать информацию с сайтов объявлений о продаже машин в России и в Европе, чтобы сравнивать цены по разным моделям и находить наиболее интересные модели, которые будет более выгодно купить за рубежом.
На текущий момент установлены  парсеры к сайтам авто.ру и autoscout24, которые загружает в базу данных следующую информацию: марка, модель, год выпуска, пробег, цена, объем двигателя. Также в модели данных заведены таблицы Age и Mileage, с помощью которых можно будет в дальнейшем фильтровать данные по группам по возрасту и пробегу автомобилей
По условиям домашнего задания база данных включена в файл gitignore. Чтобы проверить работу сайта, необходимо сначала запустить команду «age», c помощью которой загрузятся справочники Age и Mileage.
Чтобы начать поиск необходимо перейти на страницу Поиск и ввести марку и модель автомобиля. При запуске поиска запускаются команды filldb (парсинг сайта авто.ру) и filldb_de (парсинг сайта autoscout24.
Данные выводятся в двух таблицах на странице Машины
В списке машин настроены ссылки, по которым можно получить детальную информацию по каждой машине. На странице с детальной информацией настроены возможности изменения и удаления данных
В планах настроить расчет таможенной пошлины для ввоза автомобиля из Европы в Россию

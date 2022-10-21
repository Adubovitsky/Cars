from django.core.management.base import BaseCommand
from app01.models import Vehicles, Age, Mileage, Location, Milgr
import requests
from bs4 import BeautifulSoup as BS


class Command(BaseCommand):

    def filldb(self, par, par2):
        class cars():
            def __init__(self, brand, model):
                self.year = 0
                self.model = model
                self.price = 0
                self.brand = brand
                self.kilometer = 0
                self.mileage = 0
                self.milgr = 0
                self.steering_wheel = "left"
                self.engine = 1100
                self.descrip = ""
                self.count = 0
                self.euro_rate = 1

            def get_exrate(self):
                url = 'https://www.cbr.ru/'
                r_rate = requests.get(url)
                html_rate = BS(r_rate.content, 'html.parser')
                res_rate = html_rate.findAll('div', class_='main-indicator_rate')
                res_rate_1 = res_rate[1].findAll('div', class_='col-md-2 col-xs-9 _right mono-num')
                rate_str = (res_rate_1[1].text)
                rate = rate_str.replace(',', '.')
                self.euro_rate = float(rate[:5])
                return self.euro_rate


            def get_keydata(self):

                pages = 15
                full_list = []
                for page in range(pages):
                    url = f"https://www.autoscout24.de/lst/{self.brand}/{self.model}?sort=standard&desc=0&ustate=N,U&atype=C&cy=D&fregfrom=2017&page={page}"    #ocs_listing=include&

                    r = requests.get(url)
                    html = BS(r.content, 'html.parser')
                    res = html.findAll('article',
                                       class_='cldt-summary-full-item listing-impressions-tracking list-page-item ListItem_article__ppamD')

                    for i in res:
                        dict = {}
                        link = i.find('a', class_='ListItem_title__znV2I Link_link__pjU1l')['href']
                        self.brand = i.get('data-make')
                        self.model = i.get('data-model')
                        self.price = int(i.get('data-price'))
                        if i.get('data-first-registration') == "new":
                            self.year = 2022
                        else:
                            try:
                                year = i.get('data-first-registration')
                                self.year = int(year[3:7])
                            except ValueError:
                                self.year = 2100

                        km = i.get('data-mileage')
                        try:
                            self.kilometer = int(km)
                        except ValueError:
                            self.kilometer = 555555

                        if self.kilometer <= 10000:
                            self.mileage = "до 10 тыс. км."
                            self.milgr = "до 30"
                        elif self.kilometer <= 20000:
                            self.mileage = "до 20 тыс. км."
                            self.milgr = "до 30"
                        elif self.kilometer <= 30000:
                            self.mileage = "до 30 тыс. км."
                            self.milgr = "до 30"
                        elif self.kilometer <= 40000:
                            self.mileage = "до 40 тыс. км."
                            self.milgr = "до 70"
                        elif self.kilometer <= 50000:
                            self.mileage = "до 50 тыс. км."
                            self.milgr = "до 70"
                        elif self.kilometer <= 60000:
                            self.mileage = "до 60 тыс. км."
                            self.milgr = "до 70"
                        elif self.kilometer <= 70000:
                            self.mileage = "до 70 тыс. км."
                            self.milgr = "до 70"
                        elif self.kilometer <= 80000:
                            self.mileage = "до 80 тыс. км."
                            self.milgr = "до 120"
                        elif self.kilometer <= 90000:
                            self.mileage = "до 90 тыс. км."
                            self.milgr = "до 120"
                        elif self.kilometer <= 100000:
                            self.mileage = "до 100 тыс. км."
                            self.milgr = "до 120"
                        elif self.kilometer <= 110000:
                            self.mileage = "до 110 тыс. км."
                            self.milgr = "до 120"
                        elif self.kilometer <= 120000:
                            self.mileage = "до 120 тыс. км."
                            self.milgr = "до 120"
                        elif self.kilometer > 120000:
                            self.mileage = "свыше 120 тыс. км."
                            self.milgr = "свыше 120"

                        res1 = i.findAll('span', class_='VehicleDetailTable_item__koEV4')
                        engine = res1[2].text
                        engine_kw = ''
                        for i in range(len(engine)):
                            if engine[i].isdigit():
                                digit = (engine[i])
                                engine_kw = engine_kw + digit
                            else:
                                break

                        self.engine = engine_kw

                        dict['брэнд'] = self.brand
                        dict['модель'] = self.model
                        dict['цена евро'] = self.price
                        dict['цена'] = self.price*self.euro_rate
                        dict['год выпуска'] = self.year
                        dict['объем двигателя'] = self.engine
                        dict['пробег'] = self.mileage
                        dict['группа пробега'] = self.milgr
                        dict['km'] = self.kilometer
                        dict['страна'] = "Европа"
                        dict['ссылка'] = 'https://www.autoscout24.de'+link
                        # dict['руль'] = self.steering_wheel

                        full_list.append(dict)
                return full_list

        brands = ["audi","bmw", "ford", "honda", "hyundai", "jeep", "kia", "lexus", "mazda", "mercedes", "nissan", "opel",
                  "skoda", "subaru", "toyota", "volkswagen", "volvo", "chevrolet", "chrysler"]

        if par in brands:
            carlist = cars(par, par2)
            carlist.get_exrate()
            return carlist.get_keydata()
        else:
            print("Введено неверное название автомобиля")

    def add_arguments(self, parser):
        parser.add_argument('par', type=str)
        parser.add_argument('par2', type=str)

    def handle(self, *args, **options):
        print('Заполнение данных автомобилей из autoscout')
        par = options['par']
        par2 = options['par2']
        data = (Command.filldb(self, par, par2))
        for i in data:
            Vehicles.objects.create(brand = i['брэнд'], model = i['модель'], pr_year = Age.objects.get(pr_year = i['год выпуска']),
                                    milage = Mileage.objects.get(name = i['пробег']), km = i['km'] , price_euro = i['цена евро'], price = i['цена'], engine = i['объем двигателя'],
                                    country = Location.objects.get(name = i['страна']), link = i['ссылка'],
                                    milgr = Milgr.objects.get(name = i['группа пробега']))


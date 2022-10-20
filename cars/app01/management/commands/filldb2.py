from django.core.management.base import BaseCommand
from app01.models import Vehicles, Age, Mileage, Location, Milgr

import requests
from bs4 import BeautifulSoup as BS

import pprint
import json

class Command(BaseCommand):

    def filldb(self, par, par2):
        class cars():
            def __init__(self, brend, model):
                self.year = 0
                self.model = model
                self.price = 0
                self.brend = brend
                self.km = 0
                self.mileage = 0
                self.milgr = 0
                self.steering_wheel = "left"
                self.engine = 0
                self.descrip = ""
                self.count = 0


            # def get_count(self):
            #     """
            #     Функция получает количество обьявлений
            #     :return:
            #     """
            #     url = f"https://auto.ru/himki/cars/{self.brend}/all/?year_from=2012&page=1"
            #     result = requests.get(url, headers=self.headers)
            #     data = result.json()
            #     count_new = data['listingSectionsCount']['new']
            #     count_used = data['listingSectionsCount']['used']
            #     self.count = count_used + count_new
            #     print(self.count)
            #     return self.count

            def get_keydata(self):
                pages = 8
                full_list = []
                for page in range(pages):
                    print('start page')
                    list = []
                    url = f'https://moscow.drom.ru/{self.brend}/{self.model}/page{page + 1}/?minyear=2017/'
                    url_low = url.lower()
                    print(url_low)
                    r = requests.get(url_low)
                    soup = BS(r.content, 'html.parser')
                    res = soup.findAll('a')  # Список блоков с машинами на одной странице


                    for i in res:

                        if i.find('div', class_="e3f4v4l2"):
                            dict = {}
                            res1 = i.find('div', class_="e3f4v4l2")
                            res1a = res1.find('span')
                            t1 = res1a.text
                            t2 = t1.replace(',', '')
                            t3 = t2.split()
                            self.brend = t3[0]
                            self.model = t3[1]
                            self.year = t3[2]
                            r = i.find('div', class_='eyvqki92')
                            res2 = r.find('span', class_="e162wx9x0")
                            res2a = res2.find('span').text
                            self.price= res2a.replace("\xa0", "")
                            self.engine = 1950

                            res3 = i.find('div', class_="e162wx9x0")
                            info = res3.findAll('span')
                            if len(info) >= 5:
                                km1 = (info[4].text)
                                km2 = km1.split()
                                if km2[0].isdigit():
                                    self.km = int(f'{km2[0]}000')
                                elif len(km2) >=2:
                                    if km2[1].isdigit():
                                        self.km = int(f'{km2[1]}000')
                            else:
                                self.km = 10

                            if self.km <= 10000:
                                self.mileage = "до 10 тыс. км."
                                self.milgr = "до 30"
                            elif self.km <= 20000:
                                self.mileage = "до 20 тыс. км."
                                self.milgr = "до 30"
                            elif self.km <= 30000:
                                self.mileage = "до 30 тыс. км."
                                self.milgr = "до 30"
                            elif self.km <= 40000:
                                self.mileage = "до 40 тыс. км."
                                self.milgr = "до 70"
                            elif self.km <= 50000:
                                self.mileage = "до 50 тыс. км."
                                self.milgr = "до 70"
                            elif self.km <= 60000:
                                self.mileage = "до 60 тыс. км."
                                self.milgr = "до 70"
                            elif self.km <= 70000:
                                self.mileage = "до 70 тыс. км."
                                self.milgr = "до 70"
                            elif self.km <= 80000:
                                self.mileage = "до 80 тыс. км."
                                self.milgr = "до 120"
                            elif self.km <= 90000:
                                self.mileage = "до 90 тыс. км."
                                self.milgr = "до 120"
                            elif self.km <= 100000:
                                self.mileage = "до 100 тыс. км."
                                self.milgr = "до 120"
                            elif self.km <= 110000:
                                self.mileage = "до 110 тыс. км."
                                self.milgr = "до 120"
                            elif self.km <= 120000:
                                self.mileage = "до 120 тыс. км."
                                self.milgr = "до 120"
                            elif self.km > 120000:
                                self.mileage = "свыше 120 тыс. км."
                                self.milgr = "свыше 120"

                            dict['брэнд'] = self.brend
                            dict['модель'] = self.model
                            dict['цена'] = self.price
                            dict['год выпуска'] = self.year
                            dict['объем двигателя'] = self.engine
                            dict['пробег'] = self.mileage
                            dict['группа пробега'] = self.milgr
                            dict['km'] = self.km
                            dict['руль'] = self.steering_wheel
                            dict['страна'] = 'Россия'

                            list.append(dict)
                    print(list)
                    print("one page printed")

                    full_list=full_list+list
                    print(full_list)
                    print(len(full_list))
                return full_list

        brands = ["audi","bmw", "ford", "honda", "hyundai", "jeep", "kia", "lexus", "mazda", "mercedes", "nissan", "opel",
                  "skoda", "subaru", "toyota", "volkswagen", "volvo", "chevrolet", "chrysler"]

        if par in brands:
            print(par, par2)
            carlist = cars(par, par2)
            # carlist.get_count()
            return carlist.get_keydata()
        else:
            print("Введено неверное название автомобиля")

    def add_arguments(self, parser):
        parser.add_argument('par', type=str)
        parser.add_argument('par2', type=str)

    def handle(self, *args, **options):
        print('Заполнение данных автомобилей из auto.ru')
        par = options['par']
        par2 = options['par2']
        data = (Command.filldb(self, par, par2))
        for i in data:
            Vehicles.objects.create(brand = i['брэнд'], model = i['модель'], pr_year = Age.objects.get(pr_year = i['год выпуска']),
                                    milage = Mileage.objects.get(name = i['пробег']), km = i['km'] , price = i['цена'], engine = i['объем двигателя'],
                                    country = Location.objects.get(name = i['страна']), milgr = Milgr.objects.get(name = i['группа пробега']) )


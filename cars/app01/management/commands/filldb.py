from django.core.management.base import BaseCommand
from app01.models import Vehicles, Age, Mileage
import requests
import pprint

class Command(BaseCommand):

    def filldb(self):
        class cars():
            def __init__(self, brend):
                self.year = 0
                self.model = ""
                self.price = 0
                self.brend = brend
                self.kilometer = 0
                self.mileage = 0
                self.steering_wheel = "left"
                self.engine = 0
                self.descrip = ""
                self.count = 0
                self.headers = {
                    "accept": "application/json",
                    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "x-csrf-token": "6f55024bf14b676b055ad065b6f5ca93df2940d8efc9c8e9",
                    "x-requested-with": "fetch",
                    "x-susanin-react": "true",
                    "cookie": "_csrf_token=6f55024bf14b676b055ad065b6f5ca93df2940d8efc9c8e9; suid=770ef9a84ee0d2054c95ff8f2a5c535c.a3dfed6905c3bd33bc38c0e68aa07117; gdpr=0; _ym_uid=1656404335957257797; autoru_sid=a%3Ag62e69e792p0paprbe6nahbet9vq15ss.edb8e9f765746bc7f7f499a08a658276%7C1659281017054.604800.2BQHmMi2uHBxpW2VMQfKPA._oA70Py-1p2iLZOcmuTBXyAEHEQ87H7qkTAAYHWrDuY; autoruuid=g62e69e792p0paprbe6nahbet9vq15ss.edb8e9f765746bc7f7f499a08a658276; counter_ga_all7=1; yuidlt=1; yandexuid=7909073061634043510; my=YwA%3D; Session_id=3:1659281020.5.0.1658910750869:K4I6ng:27.1.2:1|628153.0.2|61:10006312.654563.zfJFLIF0XbuCxk-XwyGS9rLRN8k; yandex_login=eermilova; ys=wprid.1656776455884601-7846651172985748379-vla1-4630-vla-l7-balancer-8080-BAL-393%23c_chck.532511505%23udn.cDrQldC60LDRgtC10YDQuNC90LAg0JDQu9C10LrRgdC10LXQstC90LA%3D#udn.cDrQldC60LDRgtC10YDQuNC90LAg0JDQu9C10LrRgdC10LXQstC90LA%3D#c_chck.3526282630; i=GUALrWqXmqbatgmgEX03NYMfrspKOdCc6xYf1l6iX2gUem1KEl1rWS0MSuc9Qd3M9eIgFZqxWdvFEs8cB9VlmxiLvS8=; mda2_beacon=1659281020752; _ym_isad=2; sso_status=sso.passport.yandex.ru:synchronized; autoru-visits-count=1; _yasc=/dYE83ClAlWESUhWQxy1qYvRIVvwxJCML80s7APYkvu6ZpsU; cycada=D7CSyVNwcOdtOi2E56cHdBSWf2EiKnaLQUudBH8T9PU=; from=google-search; _ym_d=1659284288; from_lifetime=1659284288791",
                    "Referer": "https://auto.ru/",
                    "Referrer-Policy": "no-referrer-when-downgrade"
                }

            def get_count(self):
                """
                Функция получает количество обьявлений
                :return:
                """
                url = f"https://auto.ru/himki/cars/{self.brend}/all/?year_from=2012&page=1"
                result = requests.get(url, headers=self.headers)
                data = result.json()
                count_new = data['listingSectionsCount']['new']
                count_used = data['listingSectionsCount']['used']
                self.count = count_used + count_new
                return self.count

            def get_keydata(self):
                pages = self.count // 37 + 1
                full_list = []
                for page in range(pages):
                    result = requests.get(f"https://auto.ru/himki/cars/{self.brend}/all/?year_from=2012&km_age_to=100000&page={page}",
                                          headers=self.headers)
                    data = result.json()
                    offers = data['listing']['offers']
                    for i in offers:
                        dict = {}
                        self.brend = i['vehicle_info']['mark_info']['name']
                        self.model = i['vehicle_info']['model_info']['name']
                        self.price = i['price_info']['price']
                        self.year = int(i['documents']['year'])
                        self.engine = i['vehicle_info']['tech_param']['displacement']
                        # self.descrip = i['vehicle_info']['tech_param']['human_name']
                        self.kilometer = i['state']['mileage']
                        if self.kilometer <= 10000:
                            self.mileage = "до 10 тыс. км."
                        elif self.kilometer <= 20000:
                            self.mileage = "до 20 тыс. км."
                        elif self.kilometer <= 30000:
                            self.mileage = "до 30 тыс. км."
                        elif self.kilometer <= 40000:
                            self.mileage = "до 40 тыс. км."
                        elif self.kilometer <= 50000:
                            self.mileage = "до 50 тыс. км."
                        elif self.kilometer <= 60000:
                            self.mileage = "до 60 тыс. км."
                        elif self.kilometer <= 70000:
                            self.mileage = "до 70 тыс. км."
                        elif self.kilometer <= 80000:
                            self.mileage = "до 80 тыс. км."
                        elif self.kilometer <= 90000:
                            self.mileage = "до 90 тыс. км."
                        elif self.kilometer <= 100000:
                            self.mileage = "до 100 тыс. км."
                        elif self.kilometer <= 110000:
                            self.mileage = "до 110 тыс. км."
                        elif self.kilometer <= 120000:
                            self.mileage = "до 120 тыс. км."
                        elif self.kilometer > 120000:
                            self.mileage = "свыше 120 тыс. км."


                        self.steering_wheel = i['vehicle_info']['steering_wheel']
                        dict['брэнд'] = self.brend
                        dict['модель'] = self.model
                        dict['цена'] = self.price
                        dict['год выпуска'] = self.year
                        dict['объем двигателя'] = self.engine
                        dict['пробег'] = self.mileage
                        dict['km'] = self.kilometer
                        dict['руль'] = self.steering_wheel

                        full_list.append(dict)
                return full_list

        brends = ["audi","bmw", "ford", "honda", "hyundai", "jeep", "kia", "lexus", "mazda", "mercedes", "nissan", "opel",
                  "skoda", "subaru", "toyota", "volkswagen", "volvo", "chevrolet", "chrysler"]
        brend = "subaru"
        if brend in brends:
            carlist = cars(brend)
            carlist.get_count()
            return carlist.get_keydata()
        else:
            print("Введено неверное название автомобиля")


    def handle(self, *args, **options):
        print('Заполнение данных автомобилей из auto.ru')
        Vehicles.objects.all().delete()
        data = (Command.filldb(self))
        for i in data:
            Vehicles.objects.create(brand = i['брэнд'], model = i['модель'], production_year = Age.objects.get(production_year = i['год выпуска']),
                                    milage = Mileage.objects.get(name = i['пробег']), km = i['km'] , price = i['цена'], engine = i['объем двигателя'] )


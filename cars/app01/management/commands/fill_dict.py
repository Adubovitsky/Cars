
from django.core.management.base import BaseCommand
from app01.models import Vehicles, Age, Location, Milgr


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('заполнение справочников возраста и пробега')
        Vehicles.objects.all().delete()
        Age.objects.all().delete()
        Mileage.objects.all().delete()
        Location.objects.all().delete()
        Milgr.objects.all().delete()
        age_table = [(2022, "новая", "до 5 лет"),
                    (2021, "до 3 лет", "до 5 лет"),
                     (2020, "до 3 лет", "до 5 лет"),
                     (2019, "до 3 лет", "до 5 лет"),
                     (2018, "до 5 лет", "до 5 лет"),
                     (2017, "до 5 лет", "до 5 лет"),
                     (2016, "до 8 лет", "до 10 лет"),
                     (2015, "до 8 лет", "до 10 лет"),
                     (2014, "до 8 лет", "до 10 лет"),
                     (2013, "до 10 лет", "до 10 лет"),
                     (2012, "до 10 лет", "до 10 лет"),
                     (2011, "до 13 лет", "до 15 лет"),
                     (2010, "до 13 лет", "до 15 лет"),
                     (2009, "до 13 лет", "до 15 лет"),
                     (2008, "до 15 лет", "до 20 лет"),
                     (2007, "до 15 лет", "до 20 лет"),
                     (2006, "до 17 лет", "до 20 лет"),
                     (2005, "до 17 лет", "до 20 лет"),
                     (2004, "до 20 лет", "до 20 лет"),
                     (2003, "до 20 лет", "до 20 лет"),
                     (2002, "до 20 лет", "до 20 лет")
                     ]
        for year in age_table:
            Age.objects.create(pr_year = year[0], age_small_scale = year[1], age_big_scale = year[2])

        mileage_table = [("до 10 тыс. км.", 'до 30'), ("до 20 тыс. км.", 'до 30'), ("до 30 тыс. км.", 'до 30'),
                         ("до 40 тыс. км.", 'до 70'), ("до 50 тыс. км.", 'до 70'), ("до 60 тыс. км.", 'до 70'),
                         ("до 70 тыс. км.", 'до 70'), ("до 80 тыс. км.", 'до 120'), ("до 90 тыс. км.", 'до 120'),
                         ("до 100 тыс. км.", 'до 120'), ("до 110 тыс. км.", 'до 120'), ("до 120 тыс. км.", 'до 120'),
                         ("свыше 120 тыс. км.", 'свыше 120')]
        for i in mileage_table:
            Mileage.objects.create(name=i[0], mil_group = i[1])

        Location.objects.create(name='Россия')
        Location.objects.create(name='Европа')

        milgr_table = ['до 30','до 70','до 120', 'свыше 120']
        for i in milgr_table:
            Milgr.objects.create(name=i)



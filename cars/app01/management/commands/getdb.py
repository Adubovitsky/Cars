from django.core.management.base import BaseCommand
from app01.models import Vehicles, Age, Mileage

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('список автомобилей в базе')

        result = Age.objects.all()
        for i in result:
            print(i)


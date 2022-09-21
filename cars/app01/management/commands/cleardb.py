from django.core.management.base import BaseCommand
from app01.models import Vehicles, Age, Mileage, Location

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('очищение базы')
        Vehicles.objects.all().delete()



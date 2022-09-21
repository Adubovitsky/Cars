from django.core.management.base import BaseCommand
from app01.models import Vehicles, Age, Mileage
from usersapp.models import Profile, SiteUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('выполняется команда')

        Profile.objects.create(info='This if profile', user=SiteUser.objects.get(email ='jim@test.ru'))

        # result = Age.objects.all()
        # for i in result:
        #     print(i)


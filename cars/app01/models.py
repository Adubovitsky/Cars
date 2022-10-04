from django.db import models
from usersapp.models import SiteUser
from django.db.models import Avg

# Create your models here.

class Age(models.Model):
    pr_year = models.IntegerField(unique=True)
    age_small_scale = models.CharField(max_length=16, default='skip')
    age_big_scale = models.CharField(max_length=16, default='skip')

    def __str__(self):
        return f"{self.pr_year}"

class Mileage(models.Model):
    name = models.CharField(max_length=16, unique=True)
    mil_group = models.CharField(max_length=16, default='skip')

    def __str__(self):
        return str(self.name)

class Milgr(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return str(self.name)


class Location(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return str(self.name)

class VehiclesRus(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(country__name ='Россия')

class VehiclesDe(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(country__name ='Европа')


class Vehicles(models.Model):
    objects = models.Manager()
    objects_rus = VehiclesRus()
    objects_de = VehiclesDe()
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32, default="not given")
    pr_year = models.ForeignKey(Age, on_delete=models.CASCADE)
    km = models.IntegerField(default=1)
    milage = models.ForeignKey(Mileage, on_delete=models.CASCADE)
    milgr = models.ForeignKey(Milgr, on_delete=models.CASCADE)
    price = models.IntegerField(default=1)
    price_euro = models.IntegerField(default=1)
    engine = models.IntegerField(default=1)
    custom_duty = models.IntegerField(default=1)
    country = models.ForeignKey(Location, on_delete=models.CASCADE)
    link = models.CharField(max_length=64)

    def __str__(self):
        # view = self.brand +" " +self.model +" " + str(self.price)+" руб." +" " + str(self.production_year)+ " "+str(self.km) + " км"
        # view = self.brand
        view = f"{self.brand}{self.price_euro}"
        return view

    def custom(self):
        return round(self.price*(0.3),0)




class Orders(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)




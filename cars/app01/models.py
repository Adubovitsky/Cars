from django.db import models
from usersapp.models import SiteUser

# Create your models here.

class Age(models.Model):
    production_year = models.IntegerField(unique=True)
    age_small_scale = models.CharField(max_length=16, default='skip')
    age_big_scale = models.CharField(max_length=16, default='skip')

    def __str__(self):
        return f"Год выпуска {self.production_year} {self.age_big_scale}"

class Mileage(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return str(self.name)

class Vehicles(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32, default="not given")
    production_year = models.ForeignKey(Age, on_delete=models.CASCADE)
    km = models.IntegerField(default=1)
    milage = models.ForeignKey(Mileage, on_delete=models.CASCADE)
    price = models.IntegerField(default=1)
    price_euro = models.IntegerField(default=1)
    engine = models.IntegerField(default=1)
    custom_duty = models.IntegerField(default=1)
    country = models.CharField(max_length=6)
    link = models.CharField(max_length=64)

    def __str__(self):
        # view = self.brand +" " +self.model +" " + str(self.price)+" руб." +" " + str(self.production_year)+ " "+str(self.km) + " км"
        # view = self.brand
        view = f"{self.brand}"
        return view

    def custom(self):
        return round(self.price*(0.3),0)

    def full_cost(self):
        if self.country == "de":
            custom_pay = self.custom()
            return self.price + custom_pay
        else:
            return self.price

class Orders(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
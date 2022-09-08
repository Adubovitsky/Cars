from django.test import TestCase
from.models import Vehicles, Age, Mileage
from faker import Faker
from mixer.backend.django import mixer
# Create your tests here.


class VehicleTestCaseMixer(TestCase):

    def setUp(self):
        self.age = mixer.blend(Age, production_year=2015, age_big_scale='более 5 лет')
        self.mile = mixer.blend(Mileage, name='more than 100k')
        self.vehicle = mixer.blend (Vehicles, brand= 'brand_mix', production_year=self.age, milage= self.mile, price=6000, country = 'de')

    def test_custom(self):
        self.assertEqual(self.vehicle.custom(), 1800)

    def test_fullcost(self):
        self.assertEqual(self.vehicle.full_cost(), 7800)

    def test_str(self):
        self.assertEqual(str(self.vehicle), 'brand_mix')
        self.assertEqual(str(self.age), 'Год выпуска 2015 более 5 лет')
        self.assertEqual(str(self.mile), 'more than 100k')


class VehicleTestCaseFaker(TestCase):

    def setUp(self):
        faker = Faker()
        self.age = Age.objects.create(production_year=2010, age_small_scale='small', age_big_scale='более 10 лет')
        self.mile = Mileage.objects.create(name='less than 50k')
        self.vehicle = Vehicles.objects.create(brand= 'brand_test', model= faker.name(), production_year=self.age, milage= self.mile, price=5000)

    def test_custom(self):
        self.assertEqual(self.vehicle.custom(), 1500)

    def test_str(self):
        self.assertEqual(str(self.vehicle), 'brand_test')
        self.assertEqual(str(self.age), 'Год выпуска 2010 более 10 лет')
        self.assertEqual(str(self.mile), 'less than 50k')






# class VehicleTestCase(TestCase):
#
#     def setUp(self):
#         self.age = Age.objects.create(production_year=2020, age_small_scale='test', age_big_scale='test')
#         self.mile = Mileage.objects.create(name='test mile')
#         self.vehicle = Vehicles.objects.create(brand='test', model='testmodel', production_year=self.age, milage= self.mile, price=10)
#
#     def test_custom1(self):
#         vehicle = Vehicles.objects.get(brand='test')
#         self.assertEqual(vehicle.custom(), 3)
#
#     def test_custom(self):
#         self.assertEqual(self.vehicle.custom(), 3)
#
#     def test_str(self):
#         self.assertEqual(str(self.vehicle), 'test')
#         self.assertEqual(str(self.age), '2020')
#         self.assertEqual(str(self.mile), 'test mile')
#

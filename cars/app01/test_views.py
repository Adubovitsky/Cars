from django.test import Client
from django.test import TestCase
from faker import Faker
from usersapp.models import SiteUser



class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/car-list/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/car-create/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/contact/', {'name':self.fake.name(),'message':self.fake.text(),
                                                  'email':self.fake.email()})
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/contact/')
        self.assertTrue('form' in response.context)

        response = self.client.get('/contact/')
        self.assertTrue('form' in response.context)

        response = self.client.get('/search/')
        self.assertTrue('form' in response.context)

        response = self.client.post('/search/')
        self.assertTrue('form' in response.context)

        response = self.client.get('/car_list/')
        self.assertTrue('cars', 'cars_de' in response.context)

    def test_login_required(self):
        SiteUser.objects.create_user(username='test_user', email='test@test.com', password='U1S2E3R4')
        response = self.client.get('/order-create/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test_user', password='U1S2E3R4')
        response = self.client.get('/order-create/')
        self.assertEqual(response.status_code, 200)
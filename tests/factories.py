import factory
from django.contrib.auth.models import User
from seller import models
from faker import Faker
fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User    
    
    username = 'username'
    password = 12345
    is_staff = True
    

class CarListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CarList
    seller_name = fake.name()
    seller_mobile = 45644
    model_name = 'model_name'
    description = fake.text()
    condtion_car = "E"
    asking_price = 10000
    manufactured_date = '2022-12-22'


class BuyerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Buyer

    car_list = factory.SubFactory(CarListFactory)
    buyer_name = 'buyer_name'
    buyer_mobile = 464644446
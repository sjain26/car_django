
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from seller.managers import SellerManager, BuyerManager


class CarList(models.Model):

    seller_name = models.CharField(max_length=50)
    seller_mobile = models.IntegerField(null=True, blank=True)
    POOR = 'P'
    FAIR = 'F'
    GOOD = 'G'
    EXCELLENT = 'E'

    CONDTION = [
        (POOR, 'poor'),
        (FAIR, 'fair'),
        (GOOD, 'good'),
        (EXCELLENT, 'excellent')]

    model_name = models.CharField(max_length=50)
    manufactured_date = models.DateField()
    description = models.TextField(max_length=200)
    condtion_car = models.CharField(
        max_length=1,
        choices=CONDTION)
    asking_price = models.IntegerField(validators=[
            MaxValueValidator(100000),
            MinValueValidator(1000)
        ])
    make_available = models.BooleanField(default=False)
    upload = models.ImageField(upload_to='templates/static', default="")
    
    #objects = models.Manager()
    sellmanager = SellerManager()  # customanager
    objects = SellerManager()


    def __str__(self):
        return self.model_name


class Buyer(models.Model):
    car_list = models.ForeignKey(
        CarList,
        on_delete=models.CASCADE,
        related_name="buyer"
        )
    buyer_name = models.CharField(max_length=50)
    buyer_mobile = models.IntegerField()
    buymanager = BuyerManager
    
    def __str__(self):
        return self.buyer_name
    
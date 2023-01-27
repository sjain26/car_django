from django.db import models
from django.core.mail import send_mail


class SellerManager(models.Manager):
    def available(self):
        query = self.get_queryset()
        avail = query.filter(make_available=True).order_by('manufactured_date')
        return avail

    def sold_car(self, id):
        query = self.get_queryset()
        sold = query.filter(pk=id).update(make_available=False)
        return sold
    
    def selled_car(self):
        query = self.get_queryset()
        sold = query.filter(make_available=False)
        return sold

    def search_car(self, word):
        query = self.get_queryset()
        re = query.filter(model_name__contains=word).values()
        return re

    def make_available(self, id):
        query = self.get_queryset()
        return query.filter(id=id).update(make_available=True)



class BuyerManager(models.Manager):
    
    def get_customer(self, id, name, mobile):
        
        # send_mail(
        #     'car sale',
        #     email_body,
        #     'd85715255f94c2',
        #     ['jainsatyam26@gmail.com', 'jainsatyam26@gmail.com'],
        #     )
        query = self.get_queryset()
        return query.update_or_create(
            car_list_id=id,
            buyer_name=name,
            buyer_mobile=mobile
            )
        
from django.contrib import admin
from seller.models import CarList, Buyer


class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'seller_mobile',
        'seller_name',
        'model_name',
        'condtion_car']


admin.site.register(CarList, ServiceAdmin)
admin.site.register(Buyer)

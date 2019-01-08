from django.contrib import admin
from . models import Product,Get,Order,Restaurant_information
# Register your models here.
admin.site.register(Product)
admin.site.register(Get)
admin.site.register(Order)
admin.site.register(Restaurant_information)
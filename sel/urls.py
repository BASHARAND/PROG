from django.conf.urls import url
from django.urls import path
from . views import product,new,Item,kitchen,done,order_control,doneo,print,cancle,cash

urlpatterns = [
    path('',new, name='new'),

    path('list/', product, name='List'),
    path('Item/<product_id>/', Item, name='Item'),
    path('kitchen/', kitchen, name='kitchen'),
    path('done/<order_id>/', done, name='done'),
    path('order_control/', order_control, name='order'),
    path('doneo/<order_id>/', doneo, name='doneo'),
    path('print/<order>/', print, name='print'),
    path('cancle/<order>/', cancle, name='cancle'),
    path('cash/', cash, name='cash'),
]
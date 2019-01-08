from django.db import models

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(blank=True, null=True, default=0)
    state = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


TITLE_CHOICES = (
    (1, 'FOOD'),
    (2, 'DRINKS'),
    (3, 'SWEETS'),
)


class Product(models.Model):
    name = models.CharField(max_length=30)
    Price = models.IntegerField(default=10)
    Type = models.IntegerField(choices=TITLE_CHOICES)
    image = models.FileField(upload_to=' Profile_image', blank=True, null=True)

    def __str__(self):
        return self.name

class Get(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=1)
    value = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(default=0)
    M=models.BooleanField(default=True)
    K = models.BooleanField(default=True)
    Sh = models.BooleanField(default=False)
    T= models.BooleanField(default=True)
    Ch= models.BooleanField(default=False)
    Pot= models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class Restaurant_information(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    address=models.TextField(max_length=40)
    logo= models.FileField(upload_to=' Profile_image', blank=True,null=True)
    def __str__(self):
        return self.name

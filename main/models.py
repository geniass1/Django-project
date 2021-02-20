from django.db import models


class Product(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.IntegerField('Price')
    task = models.TextField('About')
    category = models.CharField(max_length=255, default="")
    image = models.ImageField(null=True, blank=True, upload_to="images/")


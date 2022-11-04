from django.db import models
from django_resized import ResizedImageField


class Product(models.Model):
    product_image = ResizedImageField(scale=0.5, upload_to='products')
    expiry_date = models.DateField()

    def __str__(self):
        return str(self.expiry_date)

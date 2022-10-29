from django.db import models


class Product(models.Model):
    product_image = models.ImageField(upload_to='products')
    expiry_date = models.DateField()

    def __str__(self):
        return str(self.expiry_date)

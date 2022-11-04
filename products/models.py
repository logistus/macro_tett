import os
from django.db import models
from django.conf import settings
from django_resized import ResizedImageField


class Product(models.Model):
    product_image = ResizedImageField(scale=0.5, upload_to='products')
    expiry_date = models.DateField()

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.product_image.name))
        super().delete()

    def __str__(self):
        return str(self.expiry_date)

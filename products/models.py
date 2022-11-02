from django.db import models
from PIL import Image
import os
from django.conf import settings


class Product(models.Model):
    product_image = models.ImageField(upload_to='products')
    expiry_date = models.DateField()

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.product_image.path)
        output_size = (150, 150)
        img.thumbnail(output_size)
        img.save(self.product_image.path)

    def delete(self, *args):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.product_image.name))
        super().delete()

    def __str__(self):
        return str(self.expiry_date)

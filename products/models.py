from django.db import models
from PIL import Image


class Product(models.Model):
    product_image = models.ImageField(upload_to='products')
    expiry_date = models.DateField()

    def save(self, *args, **kwargs):
        if self.product_image:
            super().save()
            img = Image.open(self.product_image.path)
            if img.height > 150 and img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(self.product_image.path)

    def __str__(self):
        return str(self.expiry_date)

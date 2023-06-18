from django.db import models
from django.utils import timezone

from django.utils.text import slugify


class Shoe(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=1000, null=True, default=None)
    category = models.CharField(max_length=1000, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, default=None)
    color = models.CharField(max_length=200, null=True, default=None)
    # tạo đường link url lấy từng đối tượng sách
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    image = models.ImageField(
        upload_to='clothes_images/', null=True, default=None)   # ảnh minh họa
    
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Shoe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ShoeInventory(models.Model):
    shoe = models.ForeignKey(
        Shoe, on_delete=models.CASCADE, related_name='sizes', null=True)
    size = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.size

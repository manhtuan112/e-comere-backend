from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Comment(models.Model):
    uname = models.CharField(max_length=250)
    product_id = models.CharField(max_length=250)
    product_type = models.CharField(max_length=20, default='Book')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # luu trong lần đầu đc tạo
    updated_at = models.DateTimeField(auto_now=True) # lưu trong các lần cập nhật
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # one to five star


def __str__(self):
    return self.uname + self.product_id

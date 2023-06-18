from django.db import models

class CartItem(models.Model):
  user_id = models.CharField(max_length=50)
  product_id = models.CharField(max_length=50)
  product_type = models.CharField(max_length=50, default='Book', null=True)
  size = models.CharField(max_length=10, default=None, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  quantity = models.IntegerField(default=1)

  def __str__(self):
        return self.user_id + self.product_id

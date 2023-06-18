from django.db import models


class OrderItem(models.Model):
    # The following are the fields of our table.
    user_id = models.IntegerField()
    cart_id = models.IntegerField()
    payment_id = models.IntegerField()


    def __str__(self):
        return self.user_id + self.cart_id
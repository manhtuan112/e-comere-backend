from django.db import models

from django.db import models


class Payment(models.Model):
    # The following are the fields of our table.
    payment_status = models.CharField(max_length=20, default='Chưa thành toán')
    payment_type = models.CharField(max_length=20, default='Bằng tiền mặt')
    credits_card_number = models.CharField(
        max_length=20, null=True, default=None)
    order_id = models.IntegerField(default=None)

    def __str__(self):
        return self.pk

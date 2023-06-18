from django.db import models


class Shipment(models.Model):
    # The following are the fields of our table.
    name = models.CharField(max_length=200)
    user_id = models.IntegerField()
    mobile = models.CharField(max_length=12)
    address = models.TextField()
    shipment_status = models.CharField(max_length=20, default='Chờ lấy hàng')
    order_id = models.IntegerField(default=1)
    price = models.FloatField(default=1)

    def __str__(self):
        return self.name + self.order_id + self.user_id


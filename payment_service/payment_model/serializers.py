from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('order_id') is None:  # validate không truyền order_id
            raise ValidationError("Payment cann't empty order_id")
        return attrs

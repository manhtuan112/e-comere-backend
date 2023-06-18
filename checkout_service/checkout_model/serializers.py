from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)



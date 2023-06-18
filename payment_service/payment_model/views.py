from django.shortcuts import render

# Create your views here.
from .models import Payment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from payment_model.serializers import PaymentSerializer
from django.shortcuts import get_object_or_404
import requests
import json


@api_view(["POST"])
def create_payment(request):
    payment_serializer = PaymentSerializer(data=request.data)
    if payment_serializer.is_valid():
        payment_serializer.save()
        return Response({
            'success': True,
            'code': 200,
            "message": "create payment successful",
            "data": payment_serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": payment_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
def get_or_update_payment_by_id(request, id):
    try:
        payment = get_object_or_404(Payment, id=id)
        # api lấy thông tin
        if request.method == 'GET':
            payment_serializer = PaymentSerializer(payment)
            return Response({
                'success': True,
                'code': 200,
                "message": "get payment successful",
                "data": payment_serializer.data
            }, status=status.HTTP_200_OK)
        # api cập nhật payment
        elif request.method == 'PUT':
            # Luu ý: không dùng đoạn code dưới đây để cập nhật từng thành phần vì đã bị vướng vào validate của serializer
            payment_serializer = PaymentSerializer(payment, data=request.data)
            if payment_serializer.is_valid():
                payment_serializer.save()
                return Response({
                    'success': True,
                    'code': 200,
                    "message": "update payment successful",
                    "data": payment_serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'success': True,
                    'code': 200,
                    "message": "update payment successful",
                    "data": payment_serializer.errors
                }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

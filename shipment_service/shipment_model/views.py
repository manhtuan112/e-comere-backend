from django.shortcuts import render

# Create your views here.
from .models import Shipment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shipment_model.serializers import ShipmentSerializer
from django.shortcuts import get_object_or_404
import requests
import json


@api_view(["POST"])
def create_shipment(request):
    shipment_serializer = ShipmentSerializer(data=request.data)
    if shipment_serializer.is_valid():
        shipment_serializer.save()
        return Response({
            'success': True,
            'code': 200,
            "message": "create shipment successful",
            "data": shipment_serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": shipment_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
def get_or_update_shipment_by_id(request, id):
    try:
        shipment = get_object_or_404(Shipment, id=id)
        # api lấy thông tin
        if request.method == 'GET':
            shipment_serializer = ShipmentSerializer(shipment)
            return Response({
                'success': True,
                'code': 200,
                "message": "get shipment successful",
                "data": shipment_serializer.data
            }, status=status.HTTP_200_OK)
        # api cập nhật shipment
        elif request.method == 'PUT':
            data = request.data
            if data.get('name'):
                shipment.name = data.get('name')
            if data.get('mobile'):
                shipment.mobile = data.get('mobile')
            if data.get('address'):
                shipment.address = data.get('address')
            if data.get('shipment_status'):
                shipment.shipment_status = data.get('shipment_status')
            if data.get('order_id'):
                shipment.order_id = data.get('order_id')
            if data.get('price'):
                shipment.price = data.get('price')
            shipment.save()
            shipment_serializer = ShipmentSerializer(shipment)
            return Response({
                'success': True,
                'code': 200,
                "message": "update shipment successful",
                "data": shipment_serializer.data
            }, status=status.HTTP_200_OK)

            # Luu ý: không dùng đoạn code dưới đây để cập nhật từng thành phần vì đã bị vướng vào validate của serializer
            # shipment_serializer = ShipmentSerializer(shipment, data=request.data)
            # if shipment_serializer.is_valid():
            #     shipment_serializer.save()
            #     return Response({
            #         'success': True,
            #         'code': 200,
            #         "message": "update shipment successful",
            #         "data": shipment_serializer.data
            #     }, status=status.HTTP_200_OK)
            # else:
            #     return Response({
            #         'success': True,
            #         'code': 200,
            #         "message": "update shipment successful",
            #         "data": shipment_serializer.errors
            #     }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_shipment_list_by_user_id(request, user_id):
    shipment = Shipment.objects.filter(user_id=user_id)
    shipment_serializer = ShipmentSerializer(shipment, many=True)
    return Response({
        'success': True,
        'code': 200,
        "message": "get list shipment by user_id successful",
        "data": shipment_serializer.data
    }, status=status.HTTP_200_OK)

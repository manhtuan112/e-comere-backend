
from .models import OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from checkout_model.serializers import OrderItemSerializer
from django.shortcuts import get_object_or_404


@api_view(["POST"])
def create_orderitem(request):
    orderitem_serializer = OrderItemSerializer(data=request.data)
    if orderitem_serializer.is_valid():
        orderitem_serializer.save()

        return Response({
            'success': True,
            'code': 200,
            "message": "create order successful",
            "data": orderitem_serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": orderitem_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def get_orderitem_list_by_user_id(request, user_id):
    orderitem = OrderItem.objects.filter(user_id=user_id)
    orderitem_serializer = OrderItemSerializer(orderitem, many=True)
    return Response({
        'success': True,
        'code': 200,
        "message": "get list orderitem by user_id successful",
        "data": orderitem_serializer.data
    }, status=status.HTTP_200_OK)

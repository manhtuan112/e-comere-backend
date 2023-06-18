from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shoe_model.serializers import InventorySerializer, ShoeSerializer, InventoryResponseSerializer, ShoeSummaryInfoSerializer
from django.shortcuts import get_object_or_404
from shoe_model.models import Shoe, ShoeInventory



@api_view(['POST'])
def create_inventory(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'success': False,
            'code': 400,
            "message": "Create inventory succesful",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_inventory(request):
    shoe_id = request.data.get('shoe_id')
    size = request.data.get('size')
    try:
        shoe_inventory = get_object_or_404(
            ShoeInventory, shoe_id=shoe_id, size=size)
        data = {
            'shoe': shoe_id,
            'size': size,
            'count': request.data.get('count')
        }
        serializer = InventorySerializer(shoe_inventory, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'code': 200,
                "message": "oke",
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'code': 400,
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_shoe(request):
    # lấy ra trường size_list nếu có
    size_list = request.data.pop('size_list', None)
    shoe = ShoeSerializer(data=request.data)
    if shoe.is_valid():
        shoe.save()
        if size_list:
            for size_item in size_list:
                data = {
                    'size': size_item.get('size'),
                    'count': size_item.get('count'),
                    'shoe': shoe.data.get('id')
                }
                inventory_serializer = InventorySerializer(data=data)
                if inventory_serializer.is_valid():
                    inventory_serializer.save()
                    print(inventory_serializer.data)
                else:
                    print(inventory_serializer.errors)
        return Response({
            'success': True,
            'code': 200,
            "message": shoe.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": shoe.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_shoe(request, slug):
    # lấy tim san pham theo slug
    try:
        shoe = get_object_or_404(Shoe, slug=slug)
        shoe_serializer = ShoeSerializer(shoe, many=False)
        size_list = ShoeInventory.objects.filter(
            shoe=shoe_serializer.data.get('id'))
        combine_data = shoe_serializer.data
        if size_list:
            size_list_serializer = InventoryResponseSerializer(size_list, many=True)
            combine_data = {
                **shoe_serializer.data,
                "inventory": size_list_serializer.data
            }
            return Response({
                'success': True,
                'code': 200,
                "message": combine_data
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'success': True,
                'code': 200,
                "message": combine_data
            }, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def get_shoe_by_id(request, id):
    try:
        shoe = get_object_or_404(Shoe, id=id)
        shoe_serializer = ShoeSummaryInfoSerializer(shoe)
        return Response({
            'success': True,
            'code': 200,
            "message": "get book data successful",
            "data": shoe_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def search_shoe(request):
    try:
        
        Key_word = request.data.get('Key_word')
        shoes = Shoe.objects.filter(
            Q(name__icontains=Key_word) | Q(description__icontains=Key_word) | Q(category__icontains=Key_word) | Q(brand__icontains=Key_word) | Q(color__icontains=Key_word))
        # lọc theo title, tên tác giả, tên thể loại và mô tả
        shoe_serializer = ShoeSerializer(shoes, many=True)
        return Response({
            'success': True,
            'code': 200,
            "message": "get shoe data successful",
            "data": shoe_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)
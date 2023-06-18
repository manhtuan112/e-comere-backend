from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from clothes_model.serializers import InventorySerializer, ClothSerializer, InventoryResponseSerializer, ClothSummaryInfoSerializer
from django.shortcuts import get_object_or_404
from clothes_model.models import ClothInventory, Cloth



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
    cloth_id = request.data.get('cloth_id')
    size = request.data.get('size')
    try:
        cloth_inventory = get_object_or_404(
            ClothInventory, cloth_id=cloth_id, size=size)
        data = {
            'cloth': cloth_id,
            'size': size,
            'count': request.data.get('count')
        }
        serializer = InventorySerializer(cloth_inventory, data=data)
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
def create_cloth(request):
    # lấy ra trường size_list nếu có
    size_list = request.data.pop('size_list', None)
    cloth = ClothSerializer(data=request.data)
    if cloth.is_valid():
        cloth.save()
        if size_list:
            for size_item in size_list:
                data = {
                    'size': size_item.get('size'),
                    'count': size_item.get('count'),
                    'cloth': cloth.data.get('id')
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
            "message": cloth.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": cloth.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_cloth(request, slug):
    # lấy tim san pham theo slug
    try:
        cloth = get_object_or_404(Cloth, slug=slug)
        cloth_serializer = ClothSerializer(cloth, many=False)
        size_list = ClothInventory.objects.filter(
            cloth=cloth_serializer.data.get('id'))
        combine_data = cloth_serializer.data
        if size_list:
            size_list_serializer = InventoryResponseSerializer(size_list, many=True)
            combine_data = {
                **cloth_serializer.data,
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
def get_cloth_by_id(request, id):
    # Tìm sách
    try:
        cloth = get_object_or_404(Cloth, id=id)
        cloth_serializer = ClothSummaryInfoSerializer(cloth)
        return Response({
            'success': True,
            'code': 200,
            "message": "get book data successful",
            "data": cloth_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def search_cloth(request):
    try:
        
        Key_word = request.data.get('Key_word')
        cloths = Cloth.objects.filter(
            Q(name__icontains=Key_word) | Q(description__icontains=Key_word) | Q(category__icontains=Key_word) | Q(brand__icontains=Key_word))
        # lọc theo title, tên tác giả, tên thể loại và mô tả
        cloth_serializer = ClothSerializer(cloths, many=True)
        return Response({
            'success': True,
            'code': 200,
            "message": "get cloth data successful",
            "data": cloth_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)
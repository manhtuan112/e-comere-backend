from .models import CartItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from cart_model.serializers import CardItemSerializer
from django.shortcuts import get_object_or_404
import requests
import json


@api_view(["POST"])
def add_to_cart(request):
    user_id = request.data.get('user_id')
    product_id = request.data.get('product_id')
    product_type = request.data.get('product_type', "Book")
    size = request.data.get('size', None)

    cart_item = CardItemSerializer(data=request.data)
    try:
        # nếu tồn tại sẵn cartitem(trùng người dùng, sản phẩm, loại sản phẩm, và trung kích thước(đối với giày, quần áo))
        cart = get_object_or_404(
            CartItem, user_id=user_id, product_id=product_id, product_type=product_type, size=size)

        quantity = request.data.get('quantity', None)
        if quantity:
            cart.quantity += int(quantity)  # nếu request chứa số lượng
        else:
            cart.quantity += 1  # nếu request không chưa số lương
        cart.save()
        cart_item = CardItemSerializer(cart)

    except Exception:
        # khi sản phẩm không có trong cart thì tạo cartitem mới
        cart_item = CardItemSerializer(data=request.data)
        if cart_item.is_valid():
            cart_item.save()
        else:
            return Response({
                'success': False,
                'code': 400,
                "message": cart_item.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    return Response({
        'success': True,
        'code': 200,
        "message": "Add to cart successful",
        "data": cart_item.data
    }, status=status.HTTP_200_OK)


@api_view(["PUT", "DELETE"])
def update_cart(request, id):
    try:
        cart = get_object_or_404(CartItem, id=id)
        if request.method == 'DELETE':  # xóa cartitem
            cart.delete()
            return Response({
                'success': True,
                'code': 200,
                "message": "Delete cart successful",
            }, status=status.HTTP_200_OK)
        elif request.method == 'PUT':  # cập nhật cartitem
            quantity = request.data.get('quantity', None)
            if quantity:  # nếu tồn tại số lượng
                if quantity == 0:  # nếu quantity = 0 thì xóa cart
                    cart.delete()
                    return Response({
                        'success': True,
                        'code': 200,
                        "message": "Delete cart successful",
                    }, status=status.HTTP_200_OK)
                else:
                    cart.quantity = quantity
                    cart.save()

            size = request.data.get('size', None)
            if size:  # cập nhật số lượng
                cart.size = size
                cart.save()
            # trong trường hợp sau khi cập nhật thì được 1 cart giống hết cart đã có trong csdl về: user, product_type, product_id, size
            # thì gộp thành 1 cart
            check_cart = list(CartItem.objects.filter(
                user_id=cart.user_id, product_id=cart.product_id, product_type=cart.product_type, size=cart.size))
            if len(check_cart) == 2:  # tồn tại 2 cartitem giống nhau
                check_cart[1].quantity += check_cart[0].quantity
                check_cart[0].delete()
                check_cart[1].save()

            return Response({
                'success': True,
                'code': 200,
                "message": "Update cart successful",
            }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def show_cart(request, user_id):
    try:
        carts = list(CartItem.objects.filter(user_id=user_id))
        list_cart = []
        for cart in carts:
            data = {}
            if cart.product_type == 'Book':  # nếu có loại sản phẩm là sách
                # lấy một số thông tin sách
                url = f"http://127.0.0.1:1001/book/get_by_id/{cart.product_id}/"
                response = requests.get(
                    url=url, headers={'Content-Type': 'application/json'})
                book_info = json.loads(response.content.decode('utf-8'))
                data['name'] = book_info['data']['title']
                data['image'] = book_info['data']['image']
                data['product_type'] = cart.product_type
                data['quantity'] = cart.quantity
                # tính giá tổng tiền của cart
                data['total_price'] = cart.quantity * \
                    float(book_info['data']['price'])
                list_cart.append(data)
            else:
                url = ''
                if cart.product_type == 'Cloth':
                    url = f"http://127.0.0.1:1002/cloth/get_by_id/{cart.product_id}/"
                else:
                    url = f"http://127.0.0.1:1003/shoe/get_by_id/{cart.product_id}/"
                response = requests.get(
                    url=url, headers={'Content-Type': 'application/json'})
                product_info = json.loads(response.content.decode('utf-8'))
                data['name'] = product_info['data']['name']
                data['image'] = product_info['data']['image']
                data['product_type'] = cart.product_type
                data['quantity'] = cart.quantity
                # tính giá tổng tiền của cart
                data['size'] = cart.size
                data['total_price'] = cart.quantity * \
                    float(product_info['data']['price'])
                list_cart.append(data)

        return Response({
            'success': True,
            'code': 200,
            "message": list_cart
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)

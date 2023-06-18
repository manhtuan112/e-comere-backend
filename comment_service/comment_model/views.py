
from .models import Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from comment_model.serializers import CommentSerializer
from django.shortcuts import get_object_or_404



@api_view(["POST"])
def create_comment(request):
    comment_serializer = CommentSerializer(data=request.data)
    if comment_serializer.is_valid():
        comment_serializer.save()
        return Response({
            'success': True,
            'code': 200,
            "message": "create comment successful",
            "data": comment_serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": comment_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
def get_or_update_comment_by_id(request, id):
    try:
        comment = get_object_or_404(Comment, id=id)
        # api lấy thông tin
        if request.method == 'GET':
            comment_serializer = CommentSerializer(comment)
            return Response({
                'success': True,
                'code': 200,
                "message": "get comment successful",
                "data": comment_serializer.data
            }, status=status.HTTP_200_OK)
        # api cập nhật comment
        elif request.method == 'PUT':
            data = request.data
            if data.get('content'):
                comment.content = data.get('content')
            if data.get('rating'):
                comment.rating = data.get('rating')
            comment.save()
            comment_serializer = CommentSerializer(comment)
            return Response({
                'success': True,
                'code': 200,
                "message": "update comment successful",
                "data": comment_serializer.data
            }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_comment_list_by_product_id(request, product_id, product_type):
    print(product_id, product_type)
    comment = Comment.objects.filter(
        product_id=product_id, product_type=product_type)
    if len(list(comment)) != 0: # nếu có comment
        # tinh rating trung binh
        avarage_rating = 0
        sum = 0
        comment_list = list(comment)
        for comment_item in comment_list:
            sum += comment_item.rating
        avarage_rating = sum / len(comment_list) 

        comment_serializer = CommentSerializer(comment, many=True)
        # kết hợp mảng comment với giá trị khác dùng enumerate cùng nếu chí là đối tượng thì dùng **serializer.data
        combine_data = {f'comment_{i}': item for i,
                        item in enumerate(comment_serializer.data)}
        combine_data['avarage_rating'] = avarage_rating
        return Response({
            'success': True,
            'code': 200,
            "message": "get list comment by product successful",
            "data": combine_data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": "not found comment"
        }, status=status.HTTP_400_BAD_REQUEST)

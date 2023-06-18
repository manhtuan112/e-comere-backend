from .models import Book
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from book_model.serializers import AuthorSerializer, CategorySerializer, PublisherSerializer, BookSerializer, BookSummaryInfoSerializer
from django.shortcuts import get_object_or_404


@api_view(["POST"])
def create_book(request):
    author_data = {
        "name": request.data.get('Author name'),
        "email": request.data.get('Author email'),
        "address": request.data.get('Author address'),
    }
    author = AuthorSerializer(data=author_data)

    category_data = {
        "name": request.data.get('Category name')
    }
    category = CategorySerializer(data=category_data)

    publisher_data = {
        "name": request.data.get('Publisher name'),
        "address": request.data.get('Publisher address')
    }
    publisher = PublisherSerializer(data=publisher_data)

    if publisher.is_valid() and category.is_valid() and author.is_valid():
        book_data = {
            'title': request.data.get('title'),
            'author': author.data,
            'category': category.data,
            'publisher': publisher.data,
            'published_date': request.data.get('published_date'),
            'price': request.data.get('price'),
            'description':  request.data.get('description'),
            'inventory': request.data.get('inventory'),
            'image': request.data.get('image')
        }
        book = BookSerializer(data=book_data)
        if book.is_valid():
            book.save()
            return Response({
                'success': True,
                'code': 200,
                "message": book.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'code': 400,
                "message": book.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": "Have errors in publisher or author or category"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_book(request, **kwargs):

    id = kwargs.get('id', '')
    try:
        book = get_object_or_404(Book, id=id)

    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)

    author_data = {
        "name": request.data.get('Author name'),
        "email": request.data.get('Author email'),
        "address": request.data.get('Author address'),
    }
    author = AuthorSerializer(data=author_data)

    category_data = {
        "name": request.data.get('Category name')
    }
    category = CategorySerializer(data=category_data)

    publisher_data = {
        "name": request.data.get('Publisher name'),
        "address": request.data.get('Publisher address')
    }
    publisher = PublisherSerializer(data=publisher_data)

    if publisher.is_valid() and category.is_valid() and author.is_valid():
        book_data = {
            'title': request.data.get('title'),
            'author': author.data,
            'category': category.data,
            'publisher': publisher.data,
            'published_date': request.data.get('published_date'),
            'price': request.data.get('price'),
            'description':  request.data.get('description'),
            'inventory': request.data.get('inventory'),
            'image': request.data.get('image')
        }

        book = BookSerializer(book, data=book_data)
        if book.is_valid():
            book.save()
            return Response({
                'success': True,
                'code': 200,
                'message': 'Update successfull',
                "data": book.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'code': 400,
                "message": book.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message": "Have errors in publisher or author or category"
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_book(request, slug):
    try:
        book = get_object_or_404(Book, slug=slug)
        book.delete()
        return Response({
            'success': True,
            'code': 200,
            "message": "Delete book successful"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def get_book(request, slug):
    # Tìm sách
    try:
        book = get_object_or_404(Book, slug=slug)
        book_serializer = BookSerializer(book)
        return Response({
            'success': True,
            'code': 200,
            "message": "get book data successful",
            "data": book_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def get_book_by_id(request, id):
    # Tìm sách
    try:
        book = get_object_or_404(Book, id=id)
        book_serializer = BookSummaryInfoSerializer(book)
        return Response({
            'success': True,
            'code': 200,
            "message": "get book data successful",
            "data": book_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def search_book(request):
    # Tìm sách
    try:
        # lọc sách với có title chứa key_word không phân biệt chữ hoa chữ thường, không phần biệt có dấu hay không dấu("ngu" thì vẫn tìm được từ "Ngữ văn 8") (dùng Q để kết hợp điều kiện với nhau: | or, & and)
        # dùng author__name để tìm kiếm sách theo tên tác giả
        Key_word = request.data.get('Key_word')
        books = Book.objects.filter(
            Q(title__icontains=Key_word) | Q(author__name__icontains=Key_word) | Q(category__name__icontains=Key_word) | Q(description__icontains=Key_word))
        # lọc theo title, tên tác giả, tên thể loại và mô tả
        book_serializer = BookSerializer(books, many=True)
        return Response({
            'success': True,
            'code': 200,
            "message": "get book data successful",
            "data": book_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_inventory(request, slug):
    try:
        book = get_object_or_404(
            Book, slug=slug)

        book.inventory = request.data.get('Inventory')
        book.save()
        return Response({
            'success': True,
            'code': 200,
            "message": "update book inventory succesful"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

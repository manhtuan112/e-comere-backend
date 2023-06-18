from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from .serializers import SignUpSerializer, UserProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from .jwtToken import create_jwt_pair_for_user

from user_register.models import User
from django.shortcuts import get_object_or_404

from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
import firebase_admin
from firebase_admin import credentials, auth
from django.conf import settings

from django.contrib.auth.hashers import check_password
from rest_framework.generics import GenericAPIView
from rest_framework import serializers

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from user_register.utils import get_user_id


@api_view(["POST"])
@permission_classes([AllowAny])
def UserRegister(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.validated_data['password'] = make_password(
        #     serializer.validated_data['password'])
        serializer.save()

        return Response({
            'success': True,
            'code': 201,
            'message': 'Register successful!',
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    else:
        return Response({
            'success': False,
            'code': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([AllowAny])
def UserLogin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(
        request,
        username=username,
        password=password
    )
    if user:
        tokens = create_jwt_pair_for_user(user)
        data = {
            'success': True,
            'code': 200,
            "message": "Login Successfull",
            "tokens": tokens}
        return Response(data, status=status.HTTP_200_OK)

    return Response({
        'success': False,
        'code': 400,
        'message': 'Username or password is incorrect!',
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    try:
        # auth_header = request.headers.get('Authorization')
        # token = auth_header.split(' ')[1]
        # decoded_token = jwt.decode(
        #     token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = get_user_id(request)
        # user = User.objects.get(id=user_id)
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user, many=False)

        return Response({
            'success': True,
            'code': 200,
            "message": "Get Profile Successfull",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error_message': str(e),
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    try:

        user_id = get_user_id(request)
        user = get_object_or_404(User, id=user_id)

        if not (request.data.get('first_name') or request.data.get('last_name') or request.data.get('email') or request.data.get('username') or request.data.get('telephoneNumber') or request.data.get('address') or request.data.get('date_of_birth') or request.data.get('role')):
            return Response({
                'success': False,
                'code': 400,
                'message': "All Fields cannot be empty",
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get('email'):
            user.email = request.data.get('email')
        if request.data.get('username'):
            user.username = request.data.get('username')
        if request.data.get('telephoneNumber'):
            user.telephoneNumber = request.data.get('telephoneNumber')
        if request.data.get('address'):
            user.address = request.data.get('address')
        if request.data.get('first_name'):
            user.first_name = request.data.get('first_name')
        if request.data.get('last_name'):
            user.last_name = request.data.get('last_name')
        if request.data.get('role'):
            user.role = request.data.get('role')
        if request.data.get('date_of_birth'):
            user.date_of_birth = request.data.get('date_of_birth')
        user.save()

        return Response({
            'success': True,
            'code': 200,
            "message": "Update Successful"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error_message': str(e),
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def change_password(request):
    try:
        
        user_id = get_user_id(request)
        # user = User.objects.get(id=user_id)
        user = get_object_or_404(User, id=user_id)

        if not (request.data.get('oldPassword') and request.data.get('newPassword')):
            return Response({
                'success': False,
                'code': 400,
                'message': "oldPassword field and newPassword field cannot be empty",
            }, status=status.HTTP_400_BAD_REQUEST)
        if (request.data.get('oldPassword') == request.data.get('newPassword')):
            return Response({
                'success': False,
                'code': 400,
                'message': "oldPassword field and newPassword must be different",
            }, status=status.HTTP_400_BAD_REQUEST)
        if user.verifyToken:
            return Response({
                'success': False,
                'code': 400,
                'message': "Unable to change the password of account supply by google and facebook",
            }, status=status.HTTP_400_BAD_REQUEST)

        if check_password(request.data.get('oldPassword'), user.password):
            user.password = make_password(request.data.get('newPassword'))
            user.save()
            return Response({
                'success': True,
                'code': 200,
                "message": "Change Password Successful"
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'code': 400,
            "message": "Password is wrong"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'error_message': str(e),
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([AllowAny])
def forget_password(request):
    username = request.data.get('username','')
    email = request.data.get('email','')
    new_password =  request.data.get('new_password','')
    try: 
        user = get_object_or_404(User, username=username, email=email)

        if user:
            user.password = make_password(new_password)
            user.save()
            return Response({
                'success': True,
                'code': 200,
                "message": "Change Password Successful"
            }, status=status.HTTP_200_OK)
    except Exception: 
        return Response({
            'success': False,
            'code': 400,
            'message': 'Not found user',
        }, status=status.HTTP_400_BAD_REQUEST)
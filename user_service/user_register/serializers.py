from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=2, write_only=True)
    verifyToken = serializers.CharField(
        max_length=200, default=None, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password",
                  "first_name", "last_name", "verifyToken"]

    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs["email"]).exists()
        username_exitsts = User.objects.filter(
            username=attrs["username"]).exists()

        if not attrs.get("first_name"):
            raise ValidationError("Don't has empty field first_name")
        if not attrs.get("last_name"):
            raise ValidationError("Don't has empty field last_name")

        if email_exists:
            raise ValidationError("Email has already been used")
        if username_exitsts:
            raise ValidationError("Username has already been used")

        return super().validate(attrs)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "role",
                  "telephoneNumber", "address", "date_of_birth"]

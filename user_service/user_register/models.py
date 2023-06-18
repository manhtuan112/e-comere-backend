from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        username = self.model.normalize_username(username)

        user = self.model(username=username, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(username=username, password=password, **extra_fields)


class User(AbstractUser):

    

    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, default=None)
    role = models.CharField(max_length=20, default="NORMAL_USER")
    telephoneNumber = models.CharField(max_length=20, default=None, null=True)
    address = models.CharField(max_length=200, default=None, null=True)
    verifyToken = models.CharField(max_length=200, default=None, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
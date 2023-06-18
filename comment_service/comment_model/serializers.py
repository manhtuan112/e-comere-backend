from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)



from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Shoe, ShoeInventory


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoeInventory
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)


class ShoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoe
        fields = ('id',
                  'name',
                  'brand',
                  "color",
                  "category",
                  'price',
                  'description',
                  'slug',  # tạo đường link url lấy từng đối tượng quần áo
                  'image')   # ảnh minh họa)

    def validate(self, attrs):
        name = attrs.get("name")
        if name:
            qs = Shoe.objects.filter(name=name)
            if self.instance:
                # nếu tồn tại đối tượng truyền vào tồn tại thì loại bỏ chúng ra khỏi bộ lọc (cho trường hợp update)
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():  # trong trường hợp tạo đối tượng mới
                raise ValidationError("Shoe with this title already exists.")
        return attrs


class InventoryResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoeInventory
        fields = ('size', 'count')

    def validate(self, attrs):
        return super().validate(attrs)


class ShoeSummaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'name',
            'price',
            'image')
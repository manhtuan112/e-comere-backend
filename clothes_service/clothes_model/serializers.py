from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Cloth, ClothInventory


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothInventory
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)


class ClothSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cloth
        fields = ('id',
                  'name',
                  'brand',
                  "category",
                  'price',
                  'description',
                  'slug',  # tạo đường link url lấy từng đối tượng quần áo
                  'image')   # ảnh minh họa)

    def validate(self, attrs):
        name = attrs.get("name")
        if name:
            qs = Cloth.objects.filter(name=name)
            if self.instance:
                # nếu tồn tại đối tượng truyền vào tồn tại thì loại bỏ chúng ra khỏi bộ lọc (cho trường hợp update)
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():  # trong trường hợp tạo đối tượng mới
                raise ValidationError("Cloth with this title already exists.")
        return attrs

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.published_date = validated_data.get(
    #         'published_date', instance.published_date)
    #     instance.price = validated_data.get(
    #         'price', instance.price)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.inventory = validated_data.get(
    #         'inventory', instance.inventory)
    #     instance.image = validated_data.get(
    #         'image', instance.image)

        # Update the nested Category instance if it exists in the validated data
        category_data = validated_data.get('category')
        if category_data:
            category_serializer = CategorySerializer(
                instance.category, data=category_data)
            if category_serializer.is_valid():
                category_serializer.save()

        # Update the nested Author instance if it exists in the validated data
        author_data = validated_data.get('author')
        if author_data:
            author_serializer = AuthorSerializer(
                instance.author, data=author_data)
            if author_serializer.is_valid():
                author_serializer.save()

        # Update the nested Publisher instance if it exists in the validated data
        publisher_data = validated_data.get('publisher')
        if publisher_data:
            publisher_serializer = PublisherSerializer(
                instance.publisher, data=publisher_data)
            if publisher_serializer.is_valid():
                publisher_serializer.save()

        instance.save()
        return instance


class InventoryResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothInventory
        fields = ('size', 'count')

    def validate(self, attrs):
        return super().validate(attrs)

class ClothSummaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = (
            'name',
            'price',
            'image')
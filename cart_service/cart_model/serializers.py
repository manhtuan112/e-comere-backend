from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import CartItem


class CardItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)


# class CategorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Category
#         fields = '__all__'

#     def validate(self, attrs):

#         # name_exists = Category.objects.filter(name=attrs["name"]).exists()

#         # if name_exists:
#         #     raise ValidationError("Category has already been exits")

#         return super().validate(attrs)


# class PublisherSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Publisher
#         fields = '__all__'

#     def validate(self, attrs):

#         # name_exists = Publisher.objects.filter(name=attrs["name"]).exists()

#         # if name_exists:
#         #     raise ValidationError("Publisher has already been exits")

#         return super().validate(attrs)


# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer(many=False)
#     category = CategorySerializer(many=False)
#     publisher = PublisherSerializer(many=False)

#     class Meta:
#         model = Book
#         fields = ('id',
#                   'title',
#                   'author',
#                   "category",
#                   'publisher',
#                   'published_date',
#                   'price',
#                   'description',
#                   'slug',  # tạo đường link url lấy từng đối tượng sách
#                   'inventory',  # số lượng tồn kho
#                   'image')   # ảnh minh họa)

#     def validate(self, attrs):
#         title = attrs.get("title")
#         if title:
#             qs = Book.objects.filter(title=title)
#             if self.instance:
#                 # nếu tồn tại đối tượng truyền vào tồn tại thì loại bỏ chúng ra khỏi bộ lọc (cho trường hợp update)
#                 qs = qs.exclude(pk=self.instance.pk)
#             if qs.exists(): # trong trường hợp tạo đối tượng mới
#                 raise ValidationError("Book with this title already exists.")
#         return attrs

#     def create(self, validated_data):

#         category_data = validated_data.pop('category')

#         category, created = Category.objects.get_or_create(
#             name=category_data.get("name"))  # Trả về đối tượng category (nếu không tồn tại thì sẽ tạo mới vào csdl)

#         author_data = validated_data.pop('author')
#         author, created = Author.objects.get_or_create(
#             name=author_data.get("name"))  # Trả về đối tượng author (nếu không tồn tại thì sẽ tạo mới vào csdl)

#         publisher_data = validated_data.pop('publisher')
#         publisher, created = Publisher.objects.get_or_create(
#             name=publisher_data.get("name"))

#         book = Book.objects.create(
#             category=category, author=author, publisher=publisher, **validated_data)

#         return book

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.published_date = validated_data.get(
#             'published_date', instance.published_date)
#         instance.price = validated_data.get(
#             'price', instance.price)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.inventory = validated_data.get(
#             'inventory', instance.inventory)
#         instance.image = validated_data.get(
#             'image', instance.image)

#         # Update the nested Category instance if it exists in the validated data
#         category_data = validated_data.get('category')
#         if category_data:
#             category_serializer = CategorySerializer(
#                 instance.category, data=category_data)
#             if category_serializer.is_valid():
#                 category_serializer.save()

#         # Update the nested Author instance if it exists in the validated data
#         author_data = validated_data.get('author')
#         if author_data:
#             author_serializer = AuthorSerializer(
#                 instance.author, data=author_data)
#             if author_serializer.is_valid():
#                 author_serializer.save()

#         # Update the nested Publisher instance if it exists in the validated data
#         publisher_data = validated_data.get('publisher')
#         if publisher_data:
#             publisher_serializer = PublisherSerializer(
#                 instance.publisher, data=publisher_data)
#             if publisher_serializer.is_valid():
#                 publisher_serializer.save()

#         instance.save()
#         return instance

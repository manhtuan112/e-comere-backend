from django.contrib import admin
from book_model.models import Book, Author, Publisher, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'inventory')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)

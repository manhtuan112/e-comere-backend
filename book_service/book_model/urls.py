from django.urls import path
from book_model.views import create_book, update_book, delete_book, get_book, search_book, update_inventory, get_book_by_id

urlpatterns = [
    path('create/', create_book, name='create_book'),
    path('update/<int:id>/', update_book, name='update_book'),
    path('delete/<slug:slug>/', delete_book, name='delete_book'),
    path('get/<slug:slug>/', get_book, name='get_book'),
    path('get_by_id/<int:id>/', get_book_by_id, name='get_book_by_id'),
    path('search/', search_book, name='search_book'),
    path('update_inventory/<slug:slug>/',
         update_inventory, name='update_inventory'),


]

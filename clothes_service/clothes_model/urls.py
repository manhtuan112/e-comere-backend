from django.urls import path
from clothes_model.views import create_inventory, update_inventory, get_cloth, create_cloth, search_cloth, get_cloth_by_id
urlpatterns = [
    path('create_inventory/', create_inventory, name='create_inventory'),
    path('update_inventory/', update_inventory, name='update_inventory'),
    path('create_cloth/', create_cloth, name='create_cloth'),
    path('get_cloth/<slug:slug>/', get_cloth, name='get_cloth'),
    path('get_by_id/<int:id>/', get_cloth_by_id, name='get_cloth'),
    path('search_cloth/', search_cloth, name='search_cloth'),


]

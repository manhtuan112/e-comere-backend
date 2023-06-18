from django.urls import path
from shoe_model.views import create_inventory, update_inventory, get_shoe, create_shoe, search_shoe, get_shoe_by_id
urlpatterns = [
    path('create_inventory/', create_inventory, name='create_inventory'),
    path('update_inventory/', update_inventory, name='update_inventory'),
    path('create_shoe/', create_shoe, name='create_shoe'),
    path('get_shoe/<slug:slug>/', get_shoe, name='get_shoe'),
    path('search_shoe/', search_shoe, name='search_shoe'),
    path('get_by_id/<int:id>/', get_shoe_by_id, name='get_cloth'),

]

from django.urls import path
from cart_model.views import add_to_cart, update_cart, show_cart

urlpatterns = [
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('update/<int:id>/', update_cart, name='update_cart'),
    path('show_cart/<int:user_id>/', show_cart, name='show_cart'),

]

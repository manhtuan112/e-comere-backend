from django.urls import path
from checkout_model.views import create_orderitem, get_orderitem_list_by_user_id

urlpatterns = [
    path('create/', create_orderitem, name='create_order'),
    path('get_list_orderitem/<int:user_id>/', get_orderitem_list_by_user_id,
         name="get_shipment_list_by_user_id")


]

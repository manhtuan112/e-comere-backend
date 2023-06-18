from django.urls import path
from shipment_model.views import create_shipment, get_or_update_shipment_by_id, get_shipment_list_by_user_id

urlpatterns = [
    path('create/', create_shipment, name='create_shipment'),
    path('get_or_update_by_id/<int:id>/', get_or_update_shipment_by_id,
         name="get_or_update_shipment_by_id"),
    path('get_list_shipment/<int:user_id>/', get_shipment_list_by_user_id,
         name="get_shipment_list_by_user_id")


]

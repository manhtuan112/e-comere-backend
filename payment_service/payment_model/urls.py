from django.urls import path
from payment_model.views import create_payment, get_or_update_payment_by_id

urlpatterns = [
    path('create/', create_payment, name='create_payment'),
    path('get_or_update_by_id/<int:id>/', get_or_update_payment_by_id,
         name="get_or_update_payment_by_id"),



]

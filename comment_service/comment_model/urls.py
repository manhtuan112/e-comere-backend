from django.urls import path, re_path
from comment_model.views import create_comment, get_or_update_comment_by_id, get_comment_list_by_product_id

urlpatterns = [
    path('create/', create_comment, name='create_comment'),
    path('get_or_update_by_id/<int:id>/', get_or_update_comment_by_id,
         name="get_or_update_comment_by_id"),
    re_path(r'^get_list_comment/(?P<product_id>\d+)/type=(?P<product_type>\w+)/$', get_comment_list_by_product_id,
            name="get_comment_list_by_product_id")


]

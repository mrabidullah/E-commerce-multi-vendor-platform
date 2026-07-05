# api_urls.py

from django.urls import path
from . import api_views


urlpatterns = [

    # HOME
    path('', api_views.home_api),

    # ALL PRODUCTS
    path('all-products/', api_views.all_products_api),

    # CATEGORY
    path(
        'category/<str:category>/',
        api_views.category_api
    ),

    # PRODUCT DETAIL
    path(
        'product/<str:category>/<int:id>/',
        api_views.product_detail_api
    ),

    # SEARCH
    path(
        'search/',
        api_views.search_api
    ),

    # ORDER
    path(
        'create-order/',
        api_views.create_order_api
    ),

    # COMMENT
    path(
        'create-comment/',
        api_views.create_comment_api
    ),
]
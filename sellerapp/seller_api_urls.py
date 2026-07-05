from django.urls import path
from . import seller_api_views

urlpatterns = [
    path('profile/', seller_api_views.profile_api, name="profile-api"),

    path('add-product/', seller_api_views.add_product_api, name="add-product-api"),
    path('inventory/', seller_api_views.product_inventory_api, name="inventory-api"),

    path('edit-product/<str:category_name>/<int:product_id>/',
        seller_api_views.edit_product_api,
        name="edit-product-api"),

    path('orders/', seller_api_views.order_management_api, name="orders-api"),

    path('delete-order/<int:order_id>/',
        seller_api_views.delete_order_api,
        name="delete-order-api"),

    path('reviews/', seller_api_views.customer_reviews_api, name="reviews-api"),

    path('reply-comment/<int:comment_id>/',
        seller_api_views.reply_comment_api,
        name="reply-comment-api"),
]
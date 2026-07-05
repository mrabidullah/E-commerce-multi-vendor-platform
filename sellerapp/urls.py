from django.urls import path
from . import views

urlpatterns = [

    path('add-product/', views.add_product, name='add_product'),
    path('inventory/', views.product_inventory, name='product_inventory'),
    path('orders/', views.order_management, name='order_management'),
    path('edit-product/<str:category_name>/<int:product_id>', views.edit_product, name='edit_product'),
    path('reviews/', views.customer_reviews, name='customer_reviews'),
    path('profile/', views.profile, name='profile'),
    path('export-csv/', views.export_orders_csv, name='export_orders_csv'),
    path("orders/delete/<int:id>/", views.delete_order, name="delete_order"),
    path('reply-to-comment/<int:comment_id>/',views.reply_to_comment, name='reply_to_comment'),

]
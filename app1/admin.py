from django.contrib import admin
from .models import (
    Electronics, Fashion, Footwear, Beauty, Home, Kitchen,
    Health, Sports, Kids, Automotive, Books,
    Groceries, Jewelry, Pets, Tools,Comment
)
from .models import order_product

# Reusable Admin Class
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'brand', 'created_time')
    search_fields = ('name', 'brand')
    list_filter = ('brand', 'created_time')
    ordering = ('-created_time',)


# Register all models
admin.site.register(Electronics, ProductAdmin)
admin.site.register(Fashion, ProductAdmin)
admin.site.register(Footwear, ProductAdmin)
admin.site.register(Beauty, ProductAdmin)
admin.site.register(Home, ProductAdmin)
admin.site.register(Kitchen, ProductAdmin)
admin.site.register(Health, ProductAdmin)
admin.site.register(Sports, ProductAdmin)
admin.site.register(Kids, ProductAdmin)
admin.site.register(Automotive, ProductAdmin)
admin.site.register(Books, ProductAdmin)
admin.site.register(Groceries, ProductAdmin)
admin.site.register(Jewelry, ProductAdmin)
admin.site.register(Pets, ProductAdmin)
admin.site.register(Tools, ProductAdmin)

# Register order_product model with a simple admin interface
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('relation_to_user', 'product_name', 'quantity', 'total_price','image1', 'created_time')
    search_fields = ('relation_to_user__username', 'product_name')
    list_filter = ('created_time',)
    ordering = ('-created_time',)

admin.site.register(order_product, OrderProductAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display=('comment_text', 'created_time')
admin.site.register(Comment, CommentAdmin)
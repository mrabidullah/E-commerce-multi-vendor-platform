from django.contrib import admin
from .models import Seller

class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shop_name', 'phone' ,'image','bio','background_image','location')
    search_fields = ('shop_name', 'user__username')
    list_filter = ('shop_name',)

admin.site.register(Seller, SellerAdmin)
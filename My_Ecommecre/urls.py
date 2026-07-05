from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    # _____________________Admin________________________________?
    path('admin/', admin.site.urls),
    
    
    #______________________________seller_urls_____________________________________________?
    path('seller/', include('sellerapp.urls')),
    
    # Seller API endpoints
    path('api/seller/', include('sellerapp.seller_api_urls')),

    # ____________________________Auth (Django default auth system)______________________________________
    path('user/', include('django.contrib.auth.urls')),

    #____________________________ Your custom authentication app_____________________________________________
    path('auth/', include(('authentication.urls', 'authentication'), namespace='authentication')),

    # ________________________________Browser reload (ONLY for dev)_______________________________________________
    path("__reload__/", include("django_browser_reload.urls")),
    
    
    #_________________________________________contact urls____________________________________________________
    
    path('contact/', include('contact.urls')), 

    # _____________________________________Main pages_________________________________________________________
    path('', views.home, name='home'),
    path('product/<str:category>/<int:id>/', views.product_detail, name='product_detail'),
    path('order/<str:category>/<int:id>/', views.order_page, name='order_page'),

    # _________________________________Categories_____________________________________________________________
    path('products/', views.all_products_page, name='all_products_page'),
    path('electronics/', views.electronics_page, name='electronics_page'),
    path('fashion/', views.fashion_page, name='fashion_page'),
    path('footwear/', views.footwear_page, name='footwear_page'),
    path('beauty/', views.beauty_page, name='beauty_page'),
    path('home-page/', views.home_page, name='home_page'),
    path('kitchen/', views.kitchen_page, name='kitchen_page'),
    path('health/', views.health_page, name='health_page'),
    path('sports/', views.sports_page, name='sports_page'),
    path('kids/', views.kids_page, name='kids_page'),
    path('automotive/', views.automotive_page, name='automotive_page'),
    path('books/', views.books_page, name='books_page'),
    path('groceries/', views.groceries_page, name='groceries_page'),
    path('jewelry/', views.jewelry_page, name='jewelry_page'),
    path('pets/', views.pets_page, name='pets_page'),
    path('tools/', views.tools_page, name='tools_page'),
    path('search/', views.search,name='search'),
    path('about/', views.about, name='about'),
    
    
    
    
    path('api/auth/', include('authentication.auth_api_urls')),
    path('api/', include('app1.api_urls')),

]

# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
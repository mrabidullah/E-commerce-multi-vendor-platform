# app1/urls.py or main urls.py

from django.urls import path
from . import views
app_name='contact'

urlpatterns = [
    path('contact/', views.contact_combined, name='contact'),


]
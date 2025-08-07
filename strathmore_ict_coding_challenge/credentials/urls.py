from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_credential, name='add_credential'),
    path('view/', views.view_credentials, name='view_credentials'),
    path('success/', views.credential_success, name='credential_success'),
    path('', views.home, name='home'),
]
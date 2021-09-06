from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user_login/', views.user_login),
    path('user_register/', views.user_register),
    path('info/', views.info),
    path('logout', views.user_logout)
]
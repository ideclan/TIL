from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('theaters/', views.theaters_index, name="theaters_index"),
    path('theaters/<int:pk>/', views.theaters_detail, name="theaters_detail"),
    path('developer/', views.developer, name="developer"),
    path('change_option/', views.change_option, name="change_option"),
    path('change_page/', views.change_page, name="change_page"),
    path('search/', views.search, name="search"),
]

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('flats', views.flats, name='flats'),
    path('<int:id>', views.flat_detail, name = 'flat_detail'),
    path('search', views.search, name='search' ),

]

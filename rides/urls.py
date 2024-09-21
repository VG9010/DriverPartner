# rides/urls.py
from django.urls import path
from django.contrib import admin
from . import views
from .views import publish_ride

urlpatterns = [
    path('add/', views.add_ride, name='add_ride'),
    path('list/', views.ride_list, name='ride_list'),
    path('publish/', views.publish_ride, name='publish_ride'),
    #path('ride/<int:pk>/', views.ride_detail, name='ride_detail'),
    path('available-rides/', views.available_rides, name='available_rides'),
    path('rides/', views.available_rides, name='available_rides'),
    path('rides/<int:ride_id>/', views.ride_detail, name='ride_detail'),
    path('publish-ride/', publish_ride, name='publish_ride'),
    path('create/', views.create_ride, name='create_ride'),
]

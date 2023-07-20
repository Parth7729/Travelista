from django.urls import path
from Places import views as Places_views
from django.conf import settings

urlpatterns = [
    path('index/', Places_views.index, name="index"),
    path('get-city-data/<str:city_name>/', Places_views.city, name="city"),
    path('get-places/<str:city_name>/', Places_views.places_to_visit, name='places_to_visit'),
    path('place/<str:city_name>/<str:place>', Places_views.get_place, name='get_place'),
    path('get-restaurants/<str:city_name>/', Places_views.get_restaurants, name='get_restaurants'),
    path('restaurant/<str:city_name>/<str:restaurant>', Places_views.get_restaurant, name='get_restaurant'),


    # path('contact/', Places_views.contact, name="contact"),
    # path('about/', Places_views.about, name="about"),
    # path('places_to_visit/<str:city_name>/', Places_views.places_to_visit, name='places_to_visit'),
    # path('food/<str:city_name>/', Places_views.food, name='food'),
    # path('abc/', Places_views.abc, name="test"),
]

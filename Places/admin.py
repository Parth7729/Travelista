from django.contrib import admin
from .models import City, Place, Restaurant

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'id')

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'id')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'id')

admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
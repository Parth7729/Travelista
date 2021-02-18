from django.contrib import admin
from .models import CityInfo, PlacesToVisit, Food

# Register your models here.
class CityInfoAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'id')

class PlacesToVisitAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'id')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'id')

admin.site.register(CityInfo, CityInfoAdmin)
admin.site.register(PlacesToVisit, PlacesToVisitAdmin)
admin.site.register(Food, FoodAdmin)
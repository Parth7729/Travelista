from rest_framework import serializers
from .models import City, Place, Restaurant

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City 
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place 
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant 
        fields = '__all__'
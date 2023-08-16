from django.shortcuts import render, redirect
from Places.Scraping import scraper
from .models import City, Place, Restaurant
from .serializers import CitySerializer, PlaceSerializer, RestaurantSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

def filter_name(name):
    return '-'.join(name.lower().split(' '))

@api_view(['GET'])
def index(request):
    data =  City.objects.all().order_by('-id')
    serializer = CitySerializer(data, many=True)
    return Response({'message':'success', 'data':serializer.data})

@api_view(['GET'])
def city(request, city_name):
    name = filter_name(city_name)
    res = {}
    
    data = Place.objects.filter(city_name=name)[:6]
    serializer_place = PlaceSerializer(data, many=True)
    res['places'] = serializer_place.data


    data = Restaurant.objects.filter(city_name=name)[:6]
    serializer_restaurant = RestaurantSerializer(data, many=True)
    res['restaurants'] = serializer_restaurant.data



    try:
        data = City.objects.get(city_name=name)
        serializer_city = CitySerializer(data)
        res['city_data'] = serializer_city.data


        return Response({'message':'success', 'data':res})
    

    except Exception as e:
        print(e)
        scraped_data = scraper.city_info(name)
        if scraped_data == {}:
            return Response({'message': 'no data found'}, 404)
        
        serializer = CitySerializer(data=scraped_data)
        if serializer.is_valid():
            serializer.save()
            res['city_data'] = scraped_data
            return Response({'message':'success', 'data':res})
        
        return Response({'message':'failed', 'data':serializer.data})
        

@api_view(['GET'])
def places_to_visit(request, city_name):
    name = filter_name(city_name)
    try:
        data = Place.objects.filter(city_name=name)
        if len(data) != 0:
            serializer = PlaceSerializer(data, many=True)
            return Response({'message':'success', 'data':serializer.data})

        else:
            scraped_data = scraper.places_to_visit(name)
            if len(scraped_data) == 0:
                return Response({'message': 'data not found'}, 404)
            
            for place in scraped_data:
                serializer = PlaceSerializer(data=place)
                if serializer.is_valid():
                    serializer.save()
            
            return Response({'message':'success', 'data':scraped_data})


    except Exception as e:
        print(e)
        return Response({'message':'failed'}, 500)
    

@api_view(['GET'])
def get_place(request, city_name, place):
    name = filter_name(city_name)
    try:
        data = Place.objects.get(city_name = name, name=place)
        serializer = PlaceSerializer(data)
        return Response({'message':'success', 'data':serializer.data})
    
    except Exception as e:
        print(e)
        return Response({'message':'data not found'}, 404)
        

@api_view(['GET'])
def get_restaurants(request, city_name):
    name = filter_name(city_name)
    try:
        data = Restaurant.objects.filter(city_name=name)
        if len(data) != 0:
            serializer = RestaurantSerializer(data, many=True)
            return Response({'message':'success', 'data':serializer.data})

        else:
            scraped_data = scraper.food(name)
            if len(scraped_data) == 0:
                return Response({'message': 'data not found'}, 404)
            
            for restaurant in scraped_data:
                serializer = RestaurantSerializer(data=restaurant)
                if serializer.is_valid():
                    serializer.save()
            
            return Response({'message':'success', 'data':scraped_data})


    except Exception as e:
        print(e)
        return Response({'message':'failed'}, 500)
    

@api_view(['GET'])
def get_restaurant(request, city_name, restaurant):
    name = filter_name(city_name)
    try:
        data = Restaurant.objects.get(city_name=name, name=restaurant)
        serializer = RestaurantSerializer(data)
        return Response({'message':'success', 'data':serializer.data})
    
    except Exception as e:
        print(e)
        return Response({'message':'data not found'}, 404)

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
    data =  City.objects.all().order_by('-id')[:6]
    serializer = CitySerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def city(request, city_name):
    name = filter_name(city_name)
    try:
        data = City.objects.get(city_name=name)
        serializer = CitySerializer(data)
        return Response(serializer.data)
    except:
        res = scraper.city_info(name)
        if res == {}:
            return Response({'message': name, 'status': 404})
        
        serializer = CitySerializer(data=res)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'success', 'data':res})
        
        return Response({'message':'failed', 'data':res})
        

@api_view(['GET'])
def places_to_visit(request, city_name):
    name = filter_name(city_name)
    try:
        data = Place.objects.filter(city_name=name)
        if len(data) != 0:
            serializer = PlaceSerializer(data, many=True)
            return Response(serializer.data)

        else:
            res = scraper.places_to_visit(name)
            if res == {}:
                return Response({'message': 'data not found', 'status': 404})
            
            for place in res.values():
                serializer = PlaceSerializer(data=place)
                if serializer.is_valid():
                    serializer.save()
            
            return Response({'message':'success', 'data':res})


    except Exception as e:
        print(e)
        return Response({'message':'failed', 'data':res})
    

@api_view(['GET'])
def get_place(request, city_name, place):
    name = filter_name(city_name)
    try:
        data = Place.objects.get(city_name = name, name=place)
        serializer = PlaceSerializer(data)
        return Response({'message':'success', 'data':serializer.data})
    
    except Exception as e:
        print(e)
        return Response({'message':'data not found', 'data':place}, 404)
        

@api_view(['GET'])
def get_restaurants(request, city_name):
    name = filter_name(city_name)
    try:
        data = Restaurant.objects.filter(city_name=name)
        if len(data) != 0:
            serializer = RestaurantSerializer(data, many=True)
            return Response({'message':'success', 'data':serializer.data})

        else:
            res = scraper.food(name)
            if res == {}:
                return Response({'message': 'data not found'}, 404)
            
            for restaurant in res.values():
                serializer = RestaurantSerializer(data=restaurant)
                if serializer.is_valid():
                    serializer.save()
            
            return Response({'message':'success', 'data':res})


    except Exception as e:
        print(e)
        return Response({'message':'failed', 'data':res})
    

@api_view(['GET'])
def get_restaurant(request, city_name, restaurant):
    name = filter_name(city_name)
    try:
        data = Restaurant.objects.get(city_name = name, name=restaurant)
        serializer = RestaurantSerializer(data)
        return Response({'message':'success', 'data':serializer.data})
    
    except Exception as e:
        print(e)
        return Response({'message':'data not found', 'data':restaurant}, 404)

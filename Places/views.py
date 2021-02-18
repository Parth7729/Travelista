from django.shortcuts import render, redirect
from .models import CityInfo, PlacesToVisit, Food
from Places.Scraping import scraper


def index(request):
    cities = {}
    city_data = ''
    try:
        city_data = CityInfo.objects.all()[:4]
        if city_data:
            for i in range(4):
                cities[i] = {'city_name': city_data[i].city_name, 'city_image_link': city_data[i].city_image_link, 'state': city_data[i].state, 'country': city_data[i].country}
    except:
        pass

    context = {'cities': cities}
    return render(request, 'Places/index.html', context)

def city(request):
    if request.GET:
        city_name = request.GET['city_name'].title().replace(' ', '-')
    else:
        return redirect('index')    

    context = {'city_name': city_name}
    if CityInfo.objects.filter(city_name=city_name).exists():
        data = CityInfo.objects.get(city_name=city_name)
        context = {'city_name': data.city_name, 'city_image_link': data.city_image_link, 'state': data.state, 'country': data.country, 'covid_details': data.covid_details, 'para': data.about_the_city}
        
    else: 
        city_info = scraper.city_info(city_name)
        
        if city_info != {}:
            instance = CityInfo(city_name=city_name, city_image_link=city_info['city_image_link'], state=city_info['state'], country=city_info['country'], covid_details=city_info['covid_details'], about_the_city=city_info['para'])
            instance.save()

            data = CityInfo.objects.get(city_name=city_name)
            context = {'city_name': data.city_name, 'city_image_link': data.city_image_link, 'state': data.state, 'country': data.country, 'covid_details': data.covid_details, 'para': data.about_the_city}

    return render(request, 'Places/city.html', context)


def places_to_visit(request, city_name=None):
    
    places = {}
    places_data = {}

    if PlacesToVisit.objects.filter(city_name=city_name).exists():
        data = PlacesToVisit.objects.get(city_name=city_name)
        places_data = {'names': data.names_of_places, 'links': data.links_of_places, 'photo_links': data.photo_links, 'info': data.about_the_places, 'total_places': data.total_places}
        
    else:
        places_data = scraper.places_to_visit(city_name)

        if places_data != {}:
            instance = PlacesToVisit(city_name=city_name, names_of_places=places_data['names'], links_of_places=places_data['links'], photo_links=places_data['photo_links'], about_the_places=places_data['info'], total_places=places_data['total_places'])
            instance.save()
    if places_data != {}: 
        for i in range(places_data['total_places']):
            places[i+1] = {'name': places_data['names'][i], 'link': places_data['links'][i], 'photo_link': places_data['photo_links'][i], 'info': places_data['info'][i]}

    context = {'places': places, 'city_name': city_name}

    return render(request, 'Places/places_to_visit.html', context)


def food(request, city_name=None):
    restaurants = {}
    restaurants_data = {}

    if Food.objects.filter(city_name=city_name).exists():
        data = Food.objects.get(city_name=city_name)
        restaurants_data = {'names': data.names_of_restaurants, 'info': data.about_the_restaurants, 'photo_links': data.photo_links, 'res_items': data.restaurant_items, 'total_restaurants': data.total_restaurants}

    else:
        restaurants_data = scraper.food(city_name)

        if restaurants_data != {}:
            instance = Food(city_name=city_name, names_of_restaurants=restaurants_data['names'], about_the_restaurants=restaurants_data['info'], photo_links=restaurants_data['photo_links'], restaurant_items=restaurants_data['res_items'], total_restaurants=restaurants_data['total_restaurants'])
            instance.save()

    if restaurants_data != {}:
        for i in range(restaurants_data['total_restaurants']):
            restaurants[i+1] = {'name': restaurants_data['names'][i], 'info': restaurants_data['info'][i], 'photo_link': restaurants_data['photo_links'][i], 'res_items': restaurants_data['res_items'][i]}
    
    context = {'restaurants': restaurants, 'city_name': city_name}

    return render(request, 'Places/food.html', context)


def contact(request):
    return render(request, 'Places/contact.html')

def about(request):
    return render(request, 'Places/about.html')

def abc(request):
    return render(request, 'Places/abc.html')
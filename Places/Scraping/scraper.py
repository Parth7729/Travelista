import requests
from bs4 import BeautifulSoup as bs


def filter_text(txt):
    return ' '.join(txt.split())

def filter_name(name):
    for i in range(len(name)):
        if (name[i] >= 'a' and name[i] <= 'z') or (name[i] >= 'A' and name[i] <= 'Z'):
            return name[i:]
    
    return name

def city_info(city_name):
    try:
        url = 'https://www.holidify.com/places/' + city_name
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')
        
        city_image_link = soup.find('div', class_= 'atf-cover-image')['style'][23:-3]

        location = soup.find('div', class_='col-12 col-lg-6 right')
        # name = filter_text(location.find('h1').text)
        # name = '-'.join(name.lower().split(' '))
        state_and_country = location.find_all('b')[1:3]
        state = filter_text(state_and_country[0].text[1:-1])
        country = filter_text(state_and_country[1].text[1:])

        contents = soup.find('div', class_='col-lg-8 pr-lg-2')
        
        about = [i.text[1:] for i in contents.find('div', class_='readMoreText').find_all('p')[0:3:2]]
        tagline = filter_text(contents.find('h3', class_="tagline").text)

        data = {'image_URL': city_image_link, 'city_name': city_name, 'state': state, 'country': country, 'about': about, 'tag': tagline}
        return data
    


    except Exception as e:
        print(e)
        return {}
    


def places_to_visit(city_name):
    try:    
        url = 'https://www.holidify.com/places/' + city_name + '/sightseeing-and-things-to-do.html'
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')
        cards = soup.find_all('div', class_="card content-card")

        places_data = {}
        

        for i in range(0, len(cards)):

            places_data[i+1] = {
                'name': filter_name(filter_text(cards[i].find('h3').text)),
                'image_URL': cards[i].find('img', class_="card-img-top lazy")['data-original'],
                'about': filter_text(cards[i].find('p', class_='card-text').text),
                'city_name': city_name
            }
        
        return places_data

    except:
        return {}
    
def food(city_name):
    try:
        url = 'https://www.holidify.com/places/' + city_name+ '/restaurants-places-to-eat-local-cuisine.html'
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')
        cards = soup.find('div', class_='row no-gutters mb-50 negative-margin-mobile').find_all('div', class_='col-12 col-md-6 pr-md-3')
        
        restaurants_data = {}

        for curr_restaurant in range(len(cards)):

            try:
                image = cards[curr_restaurant].img['data-original']
            except:
                image = ''

            name = filter_name(filter_text(cards[curr_restaurant].find('h3').text))
            about = filter_text(cards[curr_restaurant].find('p').text)

            restaurant_items = cards[curr_restaurant].find('div', class_='restaurantItems').find_all('div')
            items = []
            for restaurant_item in restaurant_items:
                txt = filter_text(restaurant_item.text)
                items.append(txt)
            
            restaurants_data[curr_restaurant+1] = {'name':name, 'about':about, 'image_URL':image, 'items':items, 'city_name':city_name}
        
        return restaurants_data

    except:
        return {}

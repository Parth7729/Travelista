import requests
from bs4 import BeautifulSoup as bs


def city_info(city_name):
    try:
        url = 'https://www.holidify.com/places/' + city_name
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')
        
        city_image_link = soup.find('div', class_= 'atf-cover-image')['style'][23:-3]

        location = soup.find('div', class_='col-12 col-lg-6 right')
        city_heading = location.find('h1').text
        state_and_country = location.find_all('b')[1:3]
        state = state_and_country[0].text[1:-1]
        country = state_and_country[1].text[1:]

        covid_details = location.find('div', class_='mb-40 font-smaller').text[6:-12].replace('  \n\t', ', ')

        contents = soup.find('div', class_='col-lg-8 pr-lg-2')
        
        para = ' '.join([i.text[1:] for i in contents.find('div', class_='readMoreText').find_all('p')[0:3:2]])

        return {'city_image_link': city_image_link, 'city_heading': city_heading, 'state': state, 'country': country, 'covid_details': covid_details, 'para': para}

    except:
        return {}


def places_to_visit(city_name):
    try:    
        url = 'https://www.holidify.com/places/' + city_name + '/sightseeing-and-things-to-do.html'
        page = requests.get(url)

        soup = bs(page.content, 'html.parser')
        cards = soup.find_all('div', class_="card content-card")

        places = {}
        total_places, lim = 0, 30
        
        headings, links, photo_links, texts = [], [], [], []

        for card in cards:

            headings.append(card.find('h3').text)

            links.append(card.find('a')['href'])

            photo_links.append(card.find('img', class_="card-img-top lazy")['data-original'])

            texts.append(card.find('p', class_='card-text').text)

            total_places += 1
            if total_places >= lim:
                break

        places = {'names': headings, 'links': links, 'photo_links': photo_links, 'info': texts, 'total_places': total_places}
        
        return places

    except:
        return {}


def food(city_name):
    try:
        url = 'https://www.holidify.com/places/' + city_name+ '/restaurants-places-to-eat-local-cuisine.html'
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')
        cards = soup.find('div', class_='row no-gutters mb-50 negative-margin-mobile').find_all('div', class_='col-12 col-md-6 pr-md-3')
        
        restaurants = {}
        total_restaurants, lim = 0, 30
        names, info, photo_links, res_items = [], [], [], []

        for card in cards:

            try:
                photo_link = card.img['data-original']
            except:
                photo_link = ''

            names.append(card.find('h3').text)
            info.append(card.find('p').text)
            photo_links.append(photo_link)
            items = []
            for i in range(4):
                try:
                    items.append(card.find('div', class_='restaurantItems').find_all('div')[i].text)
                except:
                    items.append('')
            res_items.append(items)

            total_restaurants += 1
            if total_restaurants >= lim:
                break
        
        restaurants = {'names': names, 'info': info, 'photo_links': photo_links, 'res_items': res_items, 'total_restaurants': total_restaurants}

        return restaurants

    except:
        return {}

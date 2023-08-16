
# A Tourist Application Programming Interface

An API offering information regarding tourist destinations, cities, or countries, including other beneficial details.

The implementation of a Beautifulsoup-based scraper automates the retrieval and storage of location data, eliminating the need for manual insertion of over 10,000 entries and builds the DB dynamically.

Technologies - **Django, DRF, Beautifulsoup, psycopg2**

Database - **PostgreSQL RDS instance AWS**

Deployed on - **AWS EC2**
## API Reference

#### Get all Cities currently in DB

```
  GET codehashira.in/api/index
```

#### Get City details

```
  GET codehashira.in/api/get-city-data/<city_name>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `city_name`      | `string` | **Required**. Name of the city |

#### Get list of all famous places for a city

```
  GET codehashira.in/api/get-places/<city_name>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `city_name`      | `string` | **Required**. Name of the city |


#### Get list of all restaurants in a city

```
  GET codehashira.in/api/get-restaurants/<city_name>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `city_name`      | `string` | **Required**. Name of the city |

#### Get details of a restaurant

```
  GET codehashira.in/api/restaurant/<city_name>/<restaurant_name>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `city_name`      | `string` | **Required**. Name of the city |
| `restaurant_name`      | `string` | **Required**. Name of the restaurant |

#### Get details of a place

```
  GET codehashira.in/api/place/<city_name>/<place_name>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `city_name`      | `string` | **Required**. Name of the city |
| `place_name`      | `string` | **Required**. Name of the place |

## Installation

clone this repo using ``` git clone https://github.com/Parth7729/Travelistat.git ```

install dependencies - ``` pip install -r requirements.txt ```

make a postgresql db and fill the credentials in settings.py file in DATABASES variable - 

``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
```

finally make migrations and migrate - 

```
python manage.py makemigrations
python manage.py migrate

```

you're all set! run the server - 

``` 
python manage.py runserver
```

    
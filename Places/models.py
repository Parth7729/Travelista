from django.db.models import Model, CharField, TextField, URLField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class City(Model):
    city_name = CharField(max_length=50, unique=True)
    image_URL = URLField(max_length=200, null=True, blank=True)
    state = CharField(max_length=200, null=True, blank=True)
    country = CharField(max_length=200, null=True, blank=True)
    about = ArrayField(TextField(null=True), null=True, blank=True)
    tag = CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city_name

class Place(Model):
    name = CharField(max_length=100)
    about = TextField(blank=True)
    image_URL = URLField(max_length=200, blank=True)
    city_name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(Model):
    name = CharField(max_length=50)
    image_URL = URLField(max_length=200, blank=True)
    items = ArrayField(CharField(max_length=200), null=True, blank=True)
    city_name = CharField(max_length=100)
    about = TextField(blank=True)

    def __str__(self):
        return self.name

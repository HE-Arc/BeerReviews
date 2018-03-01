from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField

DEFAULT_LENGTH = 100
URL_LENGTH = 255

class StyleManager(models.Manager):
    """ Used by fixtures to resolve natural keys """
    def get_by_natural_key(self, name):
        return [self.get(name = name)]

class MakerManager(models.Manager):
    """ Used by fixtures to resolve natural keys """
    def get_by_natural_key(self, name):
        return [self.get(name = name)]

class Style(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

class Maker(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

class Beer(models.Model):
    """ What did you expect ? """
    name = models.CharField(max_length = DEFAULT_LENGTH)
    description = models.TextField()
    abv = models.FloatField(null=True) #Alcool by volume
    ebc = models.IntegerField(null=True) #European Brewery Convention
    ibu = models.IntegerField(null=True) #International Bitterness Unit
    style = models.ForeignKey(Style, on_delete = models.CASCADE)
    maker = models.ForeignKey(Maker, on_delete = models.CASCADE)
    country = CountryField(blank_label='(select country)')
    imgsrc = models.CharField(max_length = URL_LENGTH, default = "https://cdn4.iconfinder.com/data/icons/proglyphs-food/512/Beer-512.png")
    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    date = models.DateField(default=timezone.now, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete = models.CASCADE)
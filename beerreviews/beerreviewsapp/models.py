from django.db import models
from django.contrib.auth.models import User

DEFAULT_LENGTH = 100

class Country(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

class Style(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

class Maker(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

class Beer(models.Model):
    """ What did you expect ? """
    name = models.CharField(max_length = DEFAULT_LENGTH)
    description = models.TextField()
    ebc = models.IntegerField()
    style = models.ForeignKey(Style, on_delete = models.CASCADE)
    maker = models.ForeignKey(Maker, on_delete = models.CASCADE)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete = models.CASCADE)

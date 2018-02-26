from django.db import models

DEFAULT_LENGTH = 100

class Beer(models.Model):
    """ What did you expect ? """
    name = models.CharField(max_length = DEFAULT_LENGTH)
    description = models.TextField()
    ebc = models.IntegerField()
    style = models.ForeignKey(Style, on_delete = models.CASCADE)
    maker = models.ForeignKey(Maker, on_delete = models.CASCADE)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)

class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User)
    beer = models.ForeignKey(Beer)

class Country(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

class Style(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

class Maker(models.Model):
    name = models.CharField(max_length = DEFAULT_LENGTH)

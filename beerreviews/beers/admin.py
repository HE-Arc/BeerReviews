from django.contrib import admin
from .models import Beer, Maker, Style, Review
# Register your models here.

admin.site.register(Beer)
admin.site.register(Maker)
admin.site.register(Style)
admin.site.register(Review)


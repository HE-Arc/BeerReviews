from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from .models import Beer

def index(request):
    return HttpResponse("Hello, world")

# Crud
### Beers
class BeerListView(generic.ListView):
    model = Beer
    def get_queryset(self):
        return Beer.objects.all()

class BeerDetailView(generic.DetailView):
    model = Beer

### Reviews

# Login

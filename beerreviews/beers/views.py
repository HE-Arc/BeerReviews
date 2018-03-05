from django.http import HttpResponse
from django.views import generic

from .models import Beer

### Beers


class BeerListView(generic.ListView):
    model = Beer

    def get_queryset(self):
        return Beer.objects.all()


class BeerDetailView(generic.DetailView):
    model = Beer


### Reviews

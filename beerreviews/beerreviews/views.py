
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from beers.models import Beer

class IndexListView(generic.ListView):
    template_name = 'beerreviews/index.html'
    context_object_name = 'latest_beers_list'

    def get_queryset(self):
        """Return the last ten published beers"""
        return Beer.objects.filter(
            created_at__lte=timezone.now()
        ).order_by('-created_at')[:10]
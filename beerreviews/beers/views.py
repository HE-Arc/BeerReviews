from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Beer, Review


### Beers


class BeerListView(generic.ListView):
    model = Beer

    def get_queryset(self):
        return Beer.objects.all()


class BeerDetailView(generic.DetailView):
    model = Beer


### Reviews
def create_review(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)
    # if not request.user.is_authenticated:
    #     return HttpResponseForbidden()
    if request.user.is_authenticated:
        review = Review(rating=request.POST['rating'], content=request.POST['comment'], beer=beer, user=request.user)
        review.save()
    else:
        return render(request, 'beers/beer_detail.html', {
            'beer': beer,
            'error_message': "You need to be logged in to rate a beer",
        })
    return HttpResponseRedirect(reverse('beers:detail', args=(beer.id,)))

from datetime import timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db.models import Q
import operator

from .models import Beer, Review


# Our beers
class BeerListView(generic.ListView):
    model = Beer

    def get_queryset(self):
        return Beer.objects.all()


# Detail of a beer
class BeerDetailView(generic.DetailView):
    model = Beer


# Random beer
def random(request):
    beer = Beer.get_random()
    return HttpResponseRedirect(reverse('beers:detail', args=(beer.id,)))


# Top 10
class TopListView(generic.ListView):
    template_name = 'beers/beer_top.html'
    context_object_name = 'top_beers_list'
    model = Beer

    def get_queryset(self):
        return Beer.objects.order_by('-rating')


@login_required
def create_review(request, beer_id):
    """Method that create a review"""
    beer = get_object_or_404(Beer, pk=beer_id)

    if request.POST['comment'] != "":
        review, is_created = Review.objects.update_or_create(beer=beer, user=request.user)
        review.rating = request.POST['rating']
        review.content = request.POST['comment']
        review.save()
        beer.save()  # Needed to update the rating field of the beer

        # User success message
        if is_created:
            messages.success(request, "You successfully created a new review")
        else:
            messages.success(request, "You successfully updated your last review")
    else:
        messages.error(request, "Your comment is empty")

    return HttpResponseRedirect(reverse('beers:detail', args=(beer.id,)))

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        beers = Beer.objects.filter(name__icontains=q)
        for e in beers:
            print(e.name)
        return render(request, 'beers/beer_search_result.html', {'result': beers, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
#def search(request):
#    return HttpResponseRedirect(reverse('Hello'))

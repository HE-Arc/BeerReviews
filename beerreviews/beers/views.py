from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Beer, Review


# Our beers
class BeerListView(generic.ListView):
    model = Beer

    def get_queryset(self):
        return Beer.objects.all()


# Detail of a beer
class BeerDetailView(generic.DetailView):
    model = Beer


# Top 10
class TopListView(generic.ListView):
    template_name = 'beers/beer_top.html'
    context_object_name = 'top_beers_list'
    model = Beer

    def get_queryset(self):
        return Beer.objects.order_by('-rating')


# Reviews
@login_required
def create_review(request, beer_id):
    beer = get_object_or_404(Beer, pk=beer_id)

    if request.POST['comment'] != "":
        review, is_created = Review.objects.update_or_create(rating=request.POST['rating'], content=request.POST['comment'], user=request.user, beer=beer)
        # review = Review(rating=request.POST['rating'], content=request.POST['comment'], beer=beer, user=request.user)
        # review.content = request.POST['comment']
        # review.rating = request.POST['rating']
        review.save()
        beer.save()
    else:
        return render(request, 'beers/beer_detail.html', {
            'beer': beer,
            'error_message': "Your review is empty",
        })
    return HttpResponseRedirect(reverse('beers:detail', args=(beer.id,)))

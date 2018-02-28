from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from beerreviewsapp.forms import SignUpForm
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

# sign up
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

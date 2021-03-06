from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from beers.models import Beer, Review
import beerreviews

# sign up
from users.forms import SignUpForm


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
    return render(request, 'users/signup.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # messages.info(request, 'Your password was successfully updated!')
            # ICI, version django, on ajoute un message !
            messages.add_message(request, messages.INFO, 'Your password was successfully updated!')
            return render(request, 'users/profile.html', {'user': request.user})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


@login_required
def profile(request):
    review = Review.objects.filter(user=request.user.id)
    beer = Beer.objects.all()
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    else:
        return render(request, 'users/profile.html', {'user': request.user, 'review': review, 'beer': beer})

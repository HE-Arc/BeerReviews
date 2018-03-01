from django.contrib import admin
from django.urls import path, include

from beerreviews import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('beers/', include('beers.urls')),
]

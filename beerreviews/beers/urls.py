from django.urls import path

from . import views

app_name = 'beers'
urlpatterns = [
    path('', views.BeerListView.as_view(), name="beers"),
    path('<int:pk>', views.BeerDetailView.as_view(), name="detail"),
]

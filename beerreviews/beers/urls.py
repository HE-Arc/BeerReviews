from django.urls import path

from . import views

app_name = 'beers'
urlpatterns = [
    path('', views.BeerListView.as_view(), name="beers"),
    path('<int:pk>/', views.BeerDetailView.as_view(), name="detail"),
    path('<int:beer_id>/review/create/', views.create_review, name="create_review"),
    path('random/', views.random, name="random"),
    path('top/', views.TopListView.as_view(), name="top"),
    #path('search/', views.SearchResult.as_view(), name="search")
    path('search/', views.search, name="search"),
]

from django.contrib import admin
from django.urls import path
from beerreviewsapp import views
from django.contrib.auth import views as auth_views
from beerreviewsapp import views as core_views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', core_views.signup, name='signup'),
    path('beers/', views.BeerListView.as_view(), name="Beers list"),
    path('beer/<pk>', views.BeerDetailView.as_view(), name="Beer detail"),
]

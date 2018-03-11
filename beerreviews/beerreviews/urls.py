from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('beers/', include('beers.urls')),
]

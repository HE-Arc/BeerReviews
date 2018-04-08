from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('beers/', include('beers.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path
from users import views as users_views

app_name = 'users'
urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', users_views.signout, name='logout'),
    path('signup/', users_views.signup, name='signup'),
    url(r'^password/$', users_views.change_password, name='change_password'),
    url(r'^profile$', users_views.profile, name='profile'),
]

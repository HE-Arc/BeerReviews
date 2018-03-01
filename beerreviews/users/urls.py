from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as users_views

app_name = 'users'
urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', users_views.signup, name='signup'),
]

from django.urls import path
from django.contrib.auth import  views as auth_views

from blog.urls import urlpatterns

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name='account/logout.html'),name='logout')
]
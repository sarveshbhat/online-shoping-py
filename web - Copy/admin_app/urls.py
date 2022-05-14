from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login_admin', views.login_admin),
    path('home_admin', views.home_admin),
    path('allot', views.allot),
    path('allots', views.allots),

]

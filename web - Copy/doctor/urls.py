from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('doc', views.doc),
    path('show', views.show),
    path('doc', views.doc),
    path('login_user', views.login_user),
    path('home', views.home),
    path('edit/<int:lic>', views.edit),
    path('update/<int:lic>', views.update),
    path('delete/<int:lic>', views.destroy),
    path('accept/<int:order_no>', views.accept),
    path('reject/<int:order_no>', views.reject),

]

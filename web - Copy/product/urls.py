from django.urls import path
from . import views

urlpatterns = [
        path('product', views.product),
        path('product_detail', views.product_detail),
        path('product_edit/<int:pid>', views.product_edit),
        path('product_update/<int:pid>', views.product_update),
        path('product_delete/<int:pid>', views.product_destroy),

]

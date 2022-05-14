from django.urls import path
from . import views

urlpatterns = [
    path('deal', views.deal),
    path('shown', views.shown),
    path('loginn', views.loginn),
    path('med_home', views.med_home),
    path('homen', views.homen),
    path('editn/<int:lic>', views.editn),
    path('updaten/<int:lic>', views.updaten),
    path('deleten/<int:lic>', views.destroyn),
    path('view/<int:lic>', views.view),
    path('bill/<int:order_no>', views.bill),
    path('bill_pdf/<int:order_no>', views.bill_pdf),
    path('supply/<int:order_no>', views.supply),
    path('supplys/<int:order_no>', views.supplys),
    path('bill', views.bill),
    ##path('pdf/'. Generatepdf.as_view()),
]

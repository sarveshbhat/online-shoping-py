from django.urls import path
from . import views

urlpatterns = [
    path('logins', views.logins),
    path('cust', views.cust),
    path('shows', views.shows),
    path('homes', views.homes),
    path('general_item_order', views.general_item_order),
    path('productfetch', views.productfetch),
    path('pload', views.pload),
    path('medicinal_order', views.medicinal_order),
    path('medicinal_order_detail', views.medicinal_order_detail),
    path('order_detail', views.order_detail),
    path('complaint_registration', views.complaint_registration),
    path('complaints', views.complaints),
    path('feedback', views.feedback),
    path('feedbacks', views.feedbacks),
    path('edits/<int:id>', views.edits),
    path('updates/<int:id>', views.updates),
    path('deletes/<int:id>', views.destroys),
    path('cont', views.cont),
    path('load', views.load),
    path('next',views.next),
    path('view/<int:comp_id>', views.view),

]

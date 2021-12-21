from django.urls import path
from . import views

app_name='servicepage'

urlpatterns = [
    path('service/',views.service, name='service'),
    path('service_details/<int:pk>',views.service_details, name='service_detailspage'),
    path('testimonial/',views.testimonial, name='testimonialpage'),
    path('category_details/<int:pk>', views.category_details, name='category_details'),
    path('team/',views.team, name='team'),
]
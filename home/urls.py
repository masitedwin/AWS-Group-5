from django.urls import path
from .views import home_view, company_view, services_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
     path('company/', company_view, name='company'),
     path('services/', services_view, name='services'),
    path('contact/', contact_view, name='contact'),
]

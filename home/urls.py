from django.urls import path
from .views import base_view, home_view, company_view, services_view

urlpatterns = [
    path('', base_view, name='base'),
    
    path('home/', home_view, name='home'),
     path('company/', company_view, name='company'),
     path('services/', services_view, name='services'),
 
]

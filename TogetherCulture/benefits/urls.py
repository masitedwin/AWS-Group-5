from django.urls import path
from .views import benefitsV

urlpatterns = [
    path('', benefitsV, name='benefits'),
    
    
] 
from django.urls import path
from .views import ModulesV

urlpatterns = [
    path('', ModulesV, name='Modules'),
    
] 
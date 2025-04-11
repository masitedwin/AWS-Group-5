from django.urls import path
from .views import EventsV

urlpatterns = [
    path('', EventsV, name='Events'),
] 
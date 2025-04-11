from django.shortcuts import render
from .models import Event


# Create your views here.
def EventsV(request):
    event_list = Event.objects.all()
    return render(request, 'Events.html', {'event_list': event_list})


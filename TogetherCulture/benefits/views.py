from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import benefits


# Create your views here.
def benefitsV(request):
    benefits_list = benefits.objects.all()
    return render(request, 'benefits.html', {'benefits_list': benefits_list})
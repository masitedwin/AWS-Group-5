from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Module


# Create your views here.
def ModulesV(request):
    module_list = Module.objects.all()
    return render(request, 'Modules.html', {'module_list': module_list})


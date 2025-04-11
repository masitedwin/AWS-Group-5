from django.shortcuts import render

def base_view(request):
    return render(request, 'base.html')

def home_view(request):
    return render(request, 'home.html')

def company_view(request):
    return render(request, 'company.html')

def services_view(request):
    return render(request, 'services.html')





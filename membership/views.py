from django.shortcuts import render
from .models import MembershipPlan

def membership(request):
    # Fetch all pricing plans from the database
    plans = MembershipPlan.objects.all()
    return render(request, 'membership.html', {'plans': plans})
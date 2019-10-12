from django.shortcuts import render
from tickets.models import Ticket


# Create your views here.
def dashboard_stats(request):
    '''
    Get objects needed for dashboard stats and display on dashboard.html
    '''
    return render(request, "dashboard.html")

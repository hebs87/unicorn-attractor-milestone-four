from django.shortcuts import render
from tickets.models import Ticket


# Create your views here.
def dashboard_stats(request):
    '''
    Get objects needed for dashboard stats and display on dashboard.html
    '''
    # BUGS
    all_bugs = Ticket.objects.filter(ticket_type=1)
    
    # FEATURES
    all_features = Ticket.objects.filter(ticket_type=2)
    
    args = {
        'all_bugs': all_bugs,
        'all_features': all_features,
    }
    
    return render(request, "dashboard.html", args)

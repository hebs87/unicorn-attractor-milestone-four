from django.shortcuts import render
from tickets.models import Ticket


# Create your views here.
def dashboard_stats(request):
    '''
    Get objects needed for dashboard stats and display on dashboard.html
    '''
    # Filter tickets by ticket_type and store in variable
    all_bugs = Ticket.objects.filter(ticket_type=1)
    all_features = Ticket.objects.filter(ticket_type=2)
    
    # TOP 5 Bugs and Features based on upvotes
    top_five_bugs = all_bugs.order_by("-upvotes")[:5]
    top_five_features = all_features.order_by("-upvotes")[:5]

    args = {
        'top_five_bugs': top_five_bugs,
        'top_five_features': top_five_features,
    }
    
    return render(request, "dashboard.html", args)

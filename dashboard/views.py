from django.shortcuts import render
from tickets.models import Ticket


# Create your views here.
def dashboard_stats(request):
    '''
    Get objects needed for dashboard stats and display on dashboard.html
    '''
    # Filter tickets by ticket_type and store in variable
    # Bugs
    all_bugs = Ticket.objects.filter(ticket_type=1)
    # Features
    all_features = Ticket.objects.filter(ticket_type=2)

    # Total count of each ticket type
    # Bugs
    total_bugs = all_bugs.count()
    # Features
    total_features = all_features.count()

    # TOP 5 Bugs and Features based on upvotes
    # Bugs
    top_five_bugs = all_bugs.order_by("-upvotes")[:5]
    # Features
    top_five_features = all_features.order_by("-upvotes")[:5]

    # Total count of each ticket type based on ticket_status
    # Bugs
    total_open_bugs = all_bugs.filter(ticket_status=1).count()
    total_in_progress_bugs = all_bugs.filter(ticket_status=2).count()
    total_closed_bugs = all_bugs.filter(ticket_status=3).count()
    # Features
    total_open_features = all_features.filter(ticket_status=1).count()
    total_in_progress_features = all_features.filter(ticket_status=2).count()
    total_closed_features = all_features.filter(ticket_status=3).count()

    args = {
        'total_bugs': total_bugs,
        'total_features': total_features,
        'top_five_bugs': top_five_bugs,
        'top_five_features': top_five_features,
        'total_open_bugs': total_open_bugs,
        'total_in_progress_bugs': total_in_progress_bugs,
        'total_closed_bugs': total_closed_bugs,
        'total_open_features': total_open_features,
        'total_in_progress_features': total_in_progress_features,
        'total_closed_features': total_closed_features,
    }

    return render(request, "dashboard.html", args)

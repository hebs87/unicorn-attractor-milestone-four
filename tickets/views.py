from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import Ticket, Comment, Upvote
from .forms import TicketForm, CommentForm, DonationForm

# Create your views here.
def view_all_tickets(request):
    '''
    View all tickets
    Allows users to filter tickets based on type or status
    '''
    tickets = Ticket.objects.all()
    
    args = {
        "tickets": tickets,
    }
    
    return render(request, "all_tickets.html", args)

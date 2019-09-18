from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import TicketType, TicketStatus, Ticket, Comment, Upvote
from .forms import TicketForm, CommentForm, DonationForm

# Create your views here.
def view_all_tickets(request):
    '''
    View all tickets
    Allows users to filter tickets based on type or status
    '''
    tickets = Ticket.objects.all()
    ticket_type_dropdown = TicketType.objects.all()
    ticket_status_dropdown = TicketStatus.objects.all()

    args = {
        "tickets": tickets,
        "ticket_type_dropdown": ticket_type_dropdown,
        "ticket_status_dropdown": ticket_status_dropdown,
    }

    return render(request, "all_tickets.html", args)


@login_required
def new_bug_ticket(request):
    '''
    Allows user to create a new bug ticket
    '''
    if request.method == "POST":
        bug_form = TicketForm(request.POST)
        # Save form and redirect user to the page for that ticket
        if bug_form.is_valid():
            bug_form.instance.user = request.user
            bug_form.instance.ticket_type_id = 1
            bug_form.instance.ticket_status_id = 1
            new_bug = bug_form.save()
            messages.success(request, f"Thanks for submitting a Bug Report!")
            return redirect(view_all_tickets)

    else:
        bug_form = TicketForm()
    
    args = {
        "bug_form": bug_form
    }
    
    return render(request, "new_bug.html", args)

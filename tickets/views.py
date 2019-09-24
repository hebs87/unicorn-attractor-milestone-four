from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from accounts.models import Profile
from .models import TicketType, TicketStatus, Ticket, Comment, Upvote
from .forms import TicketForm, CommentForm, DonationForm
import stripe

# Create your views here.
# Import the Stripe Secret API key
stripe.api_key = settings.STRIPE_SECRET

def view_all_tickets(request):
    '''
    View all tickets
    Allows users to filter tickets based on type or status
    '''
    tickets = Ticket.objects.all()
    page = request.GET.get('page', 1)
    ticket_type_dropdown = TicketType.objects.all()
    ticket_status_dropdown = TicketStatus.objects.all()

    # Query parameters
    ticket_type = request.GET.get("ticket_type")
    ticket_status = request.GET.get("ticket_status")

    # Filter by query parameters
    if ticket_type:
        tickets = tickets.filter(ticket_type__id=ticket_type)
    else:
        tickets
    
    if ticket_status:
        tickets = tickets.filter(ticket_status__id=ticket_status)
    else:
        tickets

    # Pagination
    paginator = Paginator(tickets, 1)
    
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except:
        tickets = paginator.page(paginator.num_pages)

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


@login_required
def new_feature_ticket(request):
    '''
    Allows user to create a new bug ticket
    '''
    if request.method=="POST":
        feature_form = TicketForm(request.POST)
        donation_form = DonationForm(request.POST)
        if feature_form.is_valid() and donation_form.is_valid():
            # Total Donation Amount
            donation_amount = 0
            donation_amount += int(request.POST.get("donation_amount"))
            try:
                # Use stripe's inbuilt API to create a customer and charge
                customer = stripe.Charge.create(
                    amount = int(donation_amount * 100),
                    currency = "GBP",
                    description = request.user.email,
                    source = request.POST["stripeToken"]
                )
            except stripe.error.CardError:
                # Display error message if card is declined
                messages.error(request, "Your card was declined!")

            # If payment is successful
            if customer.paid:
                feature_form.instance.user = request.user
                feature_form.instance.ticket_type_id = 2
                feature_form.instance.total_donations = donation_amount
                # Add the donation to the user's total_donated amount
                # Get the user's current donations...
                user_total_donated = Profile.objects.values_list(
                    "total_donated", flat=True).get(user_id=request.user.id)
                # Add it to the donation amount
                new_total_donated = user_total_donated + donation_amount
                # Push the new amount to the user's total_donated amount
                Profile.objects.filter(user_id=request.user.id).update(
                    total_donated=new_total_donated)
                # Update the ticket's status to In Progress if user donates
                # the goal amount for the feature to be implemented
                if donation_amount >= int(100):
                    feature_form.instance.ticket_status_id = 2
                else:
                    # If goal amount not reached, update status to Open
                    feature_form.instance.ticket_status_id = 1
                new_feature = feature_form.save()
                messages.success(request, f"Thanks for submitting a \
                                 Feature Request!")
                return redirect(view_all_tickets)
            else:
                messages.error(request, "Unable to take payment")
        # If feature_form or donation_form aren't valid
        else:
            messages.error(request, f"We were unable to take a payment with \
                           that card. Please try again.")
    else:
        feature_form = TicketForm()
        donation_form = DonationForm()

    args = {
        "feature_form": feature_form,
        "donation_form": donation_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }

    return render(request, "new_feature.html", args)


def view_single_ticket(request, pk):
    '''
    Allows user to view the full details of a single ticket
    Returns single ticket based on ticket ID (pk) and renders it to the
    single_ticket.html template, or returns 404 error if object isn't found
    '''
    # Get the ticket details
    ticket = get_object_or_404(Ticket, pk=pk)

    args = {
        "ticket": ticket,
    }

    return render(request, "single_ticket.html", args)

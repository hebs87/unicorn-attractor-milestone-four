from django import forms
from datetime import datetime
from .models import Ticket, Comment

class TicketForm(forms.ModelForm):
    '''
    Form that allows users to create new tickets (bugs or features)
    '''
    title = forms.CharField(
        label="Ticket Title",
        min_length=5,
        max_length=100,
        widget=forms.TextInput(),
        required=True)
    description = forms.CharField(
        label="Ticket Details",
        min_length=10,
        max_length=2000,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Ticket
        fields = ["title", "description"]


class DonationForm(forms.Form):
    '''
    Allows users to select a donation amount
    This is only used when adding or upvoting feature tickets
    Offers users a list of donation amounts, in multiples of 5
    '''
    DONATION_AMOUNT_CHOICES = [(i, i) for i in range(5, 100, 5)]

    donation_amount = forms.ChoiceField(
        label="Donation Amount",
        required=False)

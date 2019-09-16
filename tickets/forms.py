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

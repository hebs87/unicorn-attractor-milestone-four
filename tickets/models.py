from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Ticket(models.Model):
    '''
    Allows users to log bug or feature tickets
    Uses CASCADE to remove ticket from user's list when deleted
    Auto-adds current date to created_date/edited_date
    '''
    # Choices for ticket type and status
    TICKET_TYPE_CHOICES = (
        ("Bug", "Bug"),
        ("Feature", "Feature"),
    )
    TICKET_STATUS_CHOICES = (
        ("Open","Open"),
        ("In Progress", "In Progress"),
        ("Closed", "Closed"),
    )

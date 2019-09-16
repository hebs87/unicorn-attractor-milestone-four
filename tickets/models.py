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
    
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    ticket_type = models.CharField(
        max_length=7,
        choices=TICKET_TYPE_CHOICES)
    ticket_status = models.CharField(
        max_length=11,
        choices=TICKET_STATUS_CHOICES)
    title = models.CharField(
        max_length=100,
        blank=False)
    description = models.TextField(
        max_length=2000,
        blank=False)
    views = models.IntegerField(
        default=0)
    upvotes = models.IntegerField(
        default=0)
    edited_date = models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now)
    total_donations = models.IntegerField(
        default=0)


    def __str__(self):
        return "#{0} [{1}] - {2}".format(
            self.ticket_type, self.ticket_status, self.title)

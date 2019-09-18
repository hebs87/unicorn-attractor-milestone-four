from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TicketType(models.Model):
    '''
    Provides the choices for the ticket type (bug or feature)
    '''
    # Choices for ticket type
    TICKET_TYPE_CHOICES = (
        ("Bug", "Bug"),
        ("Feature", "Feature"),
    )
    ticket_type = models.CharField(
        max_length=7,
        unique=True,
        choices=TICKET_TYPE_CHOICES)
    
    def __str__(self):
        return self.ticket_type


class TicketStatus(models.Model):
    '''
    Provides the choices for the ticket status (Open, In Progress or Closed)
    '''
    # Choices for ticket status
    TICKET_STATUS_CHOICES = (
        ("Open","Open"),
        ("In Progress", "In Progress"),
        ("Closed", "Closed"),
    )
    ticket_status = models.CharField(
        max_length=11,
        unique=True,
        choices=TICKET_STATUS_CHOICES)

    
    def __str__(self):
        return self.ticket_status


class Ticket(models.Model):
    '''
    Allows users to log bug or feature tickets
    Uses CASCADE to remove ticket from user's list when deleted
    Auto-adds current date to created_date/edited_date
    '''
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    ticket_type = models.ForeignKey(
        TicketType,
        null=True)
    ticket_status = models.ForeignKey(
        TicketStatus,
        null=True)
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

    class Meta:
        ordering = ("upvotes", )


    def __str__(self):
        return "#{0} [{1} - {2}] - {3}".format(
            self.id, self.ticket_type, self.ticket_status, self.title)

class Comment(models.Model):
    '''
    Allows user to comment on any ticket
    Uses CASCADE to remove comment from user's list and ticket when deleted
    '''
    
    comment_date = models.DateTimeField(
        auto_now_add=True)
    ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    description = models.TextField(
        max_length=2000,
        blank=False,
        null=True)


    def __str__(self):
        return "Comment by {0} on Ticket #{1}".format(
            self.user.username, self.ticket.id)

class Upvote(models.Model):
    '''
    Allows users to upvote any ticket
    '''
    ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)


    def __str__(self):
        return "Upvoted by {0} on Ticket #{1}".format(
            self.user.username, self.ticket.id)

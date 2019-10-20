from django.test import TestCase
from .forms import TicketForm, DonationForm, CommentForm


# Create your tests here.
class TestTicketForm(TestCase):
    def test_user_can_create_ticket(self):
        '''
        Tests that the user can create a new ticket by entering a title and
        a description
        '''
        form = TicketForm({
            "title": "Test Ticket Title",
            "description": "Test ticket description"
        })
        self.assertTrue(form.is_valid())


    def test_blank_field_error_message(self):
        '''
        Tests that the fields are required for the form to be valid
        '''
        form = TicketForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"],
                         [u"This field is required."])

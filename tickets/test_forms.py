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


class TestDonationForm(TestCase):
    def test_user_can_donate(self):
        '''
        Tests that the user can donate by selecting a donation amount
        '''
        form = DonationForm({"donation_amount": 5})
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):
    def test_user_can_create_comment_over_five_characters(self):
        '''
        Tests that the user can create a comment by filling the CommentForm,
        as long as the comment is over 5 characters
        '''
        form = CommentForm({"description": "Test comment"})
        self.assertTrue(form.is_valid())


    def test_user_cannot_create_comment_under_five_characters(self):
        '''
        Tests that the user cannot create a comment by filling the
        CommentForm, if the comment length is under 5 characters
        '''
        form = CommentForm({"description": "Test"})
        self.assertFalse(form.is_valid())


    def test_blank_field_error_message(self):
        '''
        Tests that the field is required for the CommentForm to be valid
        '''
        form = CommentForm({"description": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["description"],
                         [u"This field is required."])

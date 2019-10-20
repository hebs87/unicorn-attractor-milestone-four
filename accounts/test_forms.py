from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


class TestUserLoginForm(TestCase):
    def test_can_log_in(self):
        '''
        Tests that the user can login with a username and password
        '''
        form = UserLoginForm({"username": "User", "password": "Password"})
        self.assertTrue(form.is_valid())


    def test_invalid_details_error_message(self):
        '''
        Tests that the fields are required for the form to be valid
        '''
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"],
                         [u"This field is required."])

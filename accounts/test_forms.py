from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


class TestUserLoginForm(TestCase):
    def test_user_can_log_in(self):
        '''
        Tests that the user can login with a username and password
        '''
        form = UserLoginForm({"username": "TestUser", "password": "Password"})
        self.assertTrue(form.is_valid())


    def test_blank_field_error_message(self):
        '''
        Tests that the fields are required for the form to be valid
        '''
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"],
                         [u"This field is required."])


class TestUserRegistrationForm(TestCase):
    def test_user_can_register(self):
        '''
        Tests that the user can register by entering the relevant details
        '''
        form = UserRegistrationForm({
            "username": "TestUser",
            "email": "user@test.com",
            "first_name": "FirstName",
            "last_name": "LastName",
            "password1": "Password",
            "password2": "Password"
        })
        self.assertTrue(form.is_valid())


    def test_blank_field_error_message(self):
        '''
        Tests that the fields are required for the form to be valid
        '''
        form = UserRegistrationForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"],
                         [u"This field is required."])

    
    def test_passwords_must_match_error(self):
        '''
        Tests that the correct error is displayed when the passwords
        do not match
        '''
        form = UserRegistrationForm({
            "password1": "Password1",
            "password2": "Password2"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password2"],
                         [u"Passwords must match"])


class TestUserUpdatForm(TestCase):
    def test_user_details_updated(self):
        '''
        Tests that the user's details are updated when the UserUpdateForm
        is submitted
        '''
        form = UserUpdateForm({
            "email": "user@test.com",
            "first_name": "FirstName",
            "last_name": "LastName"
        })
        form.save()
        self.assertTrue(form.is_valid())


class TestProfileUpdateForm(TestCase):
    def test_user_can_upload_profile_image(self):
        '''
        Tests that the user can upload an image file using the
        ProfileUpdateForm
        '''
        image = ProfileUpdateForm
        image.image = SimpleUploadedFile("image.jpg",
            b"file_content", content_type="image/jpg")
        self.client.post(reverse('profile'), {"image": image})
        self.assertIsNotNone(ProfileUpdateForm)

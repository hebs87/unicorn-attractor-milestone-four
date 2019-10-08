from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

# Create a new form object
class UserLoginForm(forms.Form):
    '''
    Form to be used to log users in
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    '''
    Form used to create and register a new user
    '''
    # Username
    username = forms.CharField(label='Username',
                               min_length=6,
                               max_length=15,
                               widget=forms.TextInput(),
                               required=True)
    # Email Address
    email = forms.CharField(label='Email Address',
                            min_length=6,
                            max_length=40,
                            widget=forms.EmailInput(),
                            required=True)
    # First Name
    first_name = forms.CharField(label='First Name',
                                 min_length=2,
                                 max_length=40,
                                 widget=forms.TextInput(),
                                 required=True)
    # First Name
    last_name = forms.CharField(label='Last Name',
                                min_length=2,
                                max_length=40,
                                widget=forms.TextInput(),
                                required=True)
    # First password entry
    password1 = forms.CharField(label="Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput,
                                required=True)
    # Confirm password with a label
    password2 = forms.CharField(label="Repeat Password",
                                min_length=6,
                                max_length=25,
                                widget=forms.PasswordInput,
                                required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


    def clean_email(self):
        '''
        Validates email field and returns clean data which we can verify        
        '''
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(
                u'That email address has already been registered.')

        return email
    
    def clean_password2(self):
        '''
        Validates password field and returns clean data which we can verify        
        '''
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError(u'Please confirm your password.')

        if password1 != password2:
            raise forms.ValidationError(u'Passwords must match')

        return password2

class UserUpdateForm(forms.ModelForm):
    '''
    Form used to update the User model
    Fields aren't required
    '''
    # Email Address
    email = forms.CharField(label='Email Address',
                            min_length=6,
                            max_length=40,
                            widget=forms.EmailInput(),
                            required=False)
    # First Name
    first_name = forms.CharField(label='First Name',
                                 min_length=2,
                                 max_length=40,
                                 widget=forms.TextInput(),
                                 required=False)
    # First Name
    last_name = forms.CharField(label='Last Name',
                                min_length=2,
                                max_length=40,
                                widget=forms.TextInput(),
                                required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    '''
    Form used to update the Profile model - for the profile image
    '''
    image = forms.ImageField(
        widget=forms.FileInput)
    
    class Meta:
        model = Profile
        fields = ['image']

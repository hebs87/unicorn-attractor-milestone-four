from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def index(request):
    '''
    Return the index.html file
    '''
    return render(request, "index.html")


def login(request):
    '''
    Return a login page and logs the user in
    '''
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            # If form is valid, we get both entered username and password
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            
            if user:
                # If details are valid, log user in and display message
                auth.login(request=request, user=user)
                messages.success(request,
                    "Welcome back, you're now logged in!")
                # Redirect user to home page once logged in
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('profile'))
            else:
                # If details don't match, display error message
                messages.error(request, "It appears those details don't \
                    match what we have, please try again.")

    else:
        # Else, we want to return a blank form
        login_form = UserLoginForm()
    
    args = {'login_form': login_form, 'next': request.GET.get('next', '')}

    return render(request, "login.html", args)


@login_required
def logout(request):
    '''
    Log the user out
    '''
    auth.logout(request)
    messages.success(request, "You were successfully logged out. \
                     Come back soon!")
    return redirect(reverse('index'))


def registration(request):
    '''
    Render the registration page
    '''
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            # If form is valid, save user's
            registration_form.save()

            # Authenicate user, save details against relevant field
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            # Log user in and redirect to profile if all checks pass
            if user:
                auth.login(request=request, user=user)
                messages.success(request, "Thanks for signing up, \
                    you're now logged in!")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Registration error, please try \
                               again.")

    else:
        registration_form = UserRegistrationForm()

    args = {'registration_form': registration_form}

    return render(request, "registration.html", args)


@login_required
def user_profile(request):
    '''
    The user's profile page
    Allows the user to update their User details and Profile image
    '''
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    
    args = {'user_form': user_form, 'profile_form':profile_form}
    
    return render(request, 'profile.html', args)

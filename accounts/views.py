from django.shortcuts import render, redirect
# from django.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import loginForm

# Create your views here


def login(request):
    #if its a post request we need to process the form data.
    if request.method == 'POST':
        #create a form instance and populated with the data from the request
        form = loginForm(request.POST)
        #check whether or not it is a valid form
        if form.is_valid():
            #authenticate user.
        #get user name and password out of request.
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)

    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})

    #     if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 #redirects to a success page
    #                 return render(request, 'contacts.html')
    #             else:
    #                 #return to a failed page
    #                 return render(request, '404.html')
    # else:
    #     return render(request, '404.html')


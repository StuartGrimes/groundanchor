from django.shortcuts import render, redirect
from .models import Contacts
from .forms import addContact
from accounts.forms import loginForm
from django.contrib.auth import authenticate
from accounts.models import User

# Create your views here.

def contactList(request):

    args = {
    'contacts': Contacts.objects.all(),
        'form': addContact,
    }

    return render(request, 'contacts.html', args)

def saveNewContact(request):
    form = addContact(request.POST)
    newContact = form.save(commit=False)
    newContact.created_by_id = request.user.id
    newContact.save()
    return redirect('/contacts')

def updateContact(request):
    recordId = request.post.get('id')
    existingContactRecord = Contacts.objects.get(pk=recordId)
    #create an instance of a form for this contact
    form = addContact(instance=existingContactRecord)
    if form.is_valid():
         form.save()






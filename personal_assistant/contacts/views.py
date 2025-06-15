from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.

def base_view(request):
    return render(request, 'base.html')

def contacts_view(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_view')
    else:
        form = ContactForm()
    return render(request, 'contacts/create_contact.html', {'form': form})
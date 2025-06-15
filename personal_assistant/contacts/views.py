from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from datetime import datetime

# Create your views here.

def base_view(request):
    return render(request, 'base.html')

def contacts_view(request):
    query = request.GET.get("q", "")
    days_str = request.GET.get("days")
    contacts = Contact.objects.all()
    if query:
        contacts = contacts.filter(first_name__icontains=query)
    if days_str and days_str.isdigit():
        days = int(days_str)
        today = datetime.today().date()
        upcoming_birthdays_list = []
        for contact in contacts:
            if contact.birthday:
                birthday_this_year = datetime.strptime(contact.birthday, "%Y-%m-%d").date().replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                if 0 <= (birthday_this_year - today).days <= days:
                    upcoming_birthdays_list.append(contact)
        contacts=upcoming_birthdays_list
    return render(request, "contacts/contacts.html", {"contacts": contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_view')
    else:
        form = ContactForm()
    return render(request, 'contacts/create_contact.html', {'form': form})

def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_view')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form, 'contact': contact})

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_view')
    return render(request, 'contacts/confirm_delete.html', {'contact': contact})
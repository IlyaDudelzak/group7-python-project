"""Views for the contacts app."""

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from datetime import datetime
# from ..news.views import news_home
import feedparser

# Create your views here.

# def base_view(request):
#     # feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
#     # news = feed.entries[:5]
#     return render(request, 'base.html',news_home(request))

def contacts_view(request):
    """
    Display a list of contacts, with optional search and birthday filtering.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered contacts list page.
    """
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
    """
    Handle creation of a new contact.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered contact creation form or redirect after creation.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_view')
    else:
        form = ContactForm()
    return render(request, 'contacts/create_contact.html', {'form': form})

def edit_contact(request, pk):
    """
    Handle editing of an existing contact.

    Args:
        request: The HTTP request object.
        pk (int): Primary key of the contact to edit.

    Returns:
        HttpResponse: Rendered contact edit form or redirect after saving.
    """
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
    """
    Handle deletion of a contact.

    Args:
        request: The HTTP request object.
        pk (int): Primary key of the contact to delete.

    Returns:
        HttpResponse: Rendered confirmation page or redirect after deletion.
    """
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:contact_view')
    return render(request, 'contacts/confirm_delete.html', {'contact': contact})
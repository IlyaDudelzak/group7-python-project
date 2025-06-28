"""
Views for the chat application.
"""

from django.shortcuts import render
from django.http import JsonResponse
import os
import google.generativeai as genai
from .forms import ChatMessageForm
from .models import ChatMessage
from contacts.models import Contact
from django.utils.crypto import get_random_string


def get_device_key(request):
    device_key = request.COOKIES.get('device_key')
    if not device_key:
        device_key = get_random_string(32)
    return device_key


def chat_view(request):
    """Render the chat interface."""
    # Filter messages by user or device_key
    if request.user.is_authenticated:
        messages = ChatMessage.objects.filter(user=request.user)
    else:
        device_key = get_device_key(request)
        messages = ChatMessage.objects.filter(device_key=device_key)

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            print(f"Received user message: {user_message}")
            if user_message == '':
                return JsonResponse({'error': 'Message cannot be empty'}, status=400)

            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                return JsonResponse({'error': 'API key not configured'}, status=500)

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))

            # Store message with user or device_key
            if request.user.is_authenticated:
                ChatMessage.objects.create(
                    role='user',
                    content=user_message,
                    user=request.user
                )
                # Fetch contacts for authenticated user
                contacts = Contact.objects.filter(user=request.user)
            else:
                device_key = get_device_key(request)
                ChatMessage.objects.create(
                    role='user',
                    content=user_message,
                    device_key=device_key
                )
                # No user, so no contacts
                contacts = []

            # Prepare contents for Gemini API
            contacts_list = list(contacts.values('first_name', 'last_name', 'email', 'phone_number', 'birthday')) if contacts else []
            if contacts_list:
                contacts_str = '\n'.join([
                    f"First Name: {c['first_name']}, Last Name: {c['last_name']}, Email: {c['email']}, Phone: {c['phone_number']}, Birthday: {c['birthday']}" for c in contacts_list
                ])
                system_prompt = f"User contacts list:\n{contacts_str}\nUser message: {user_message}"
            else:
                system_prompt = user_message
            contents = [system_prompt]
            response = model.generate_content(contents=contents)

            # Save assistant message
            if request.user.is_authenticated:
                ChatMessage.objects.create(
                    role='assistant',
                    content=response.text,
                    user=request.user
                )
            else:
                device_key = get_device_key(request)
                ChatMessage.objects.create(
                    role='assistant',
                    content=response.text,
                    device_key=device_key
                )

            resp = render(request, 'chat/chat.html', {'messages': messages, "form": ChatMessageForm()})
            if not request.user.is_authenticated:
                resp.set_cookie('device_key', get_device_key(request))
            return resp
        # Handle the 'Clear Chat' button functionality
        if request.method == 'POST' and 'clear_chat' in request.POST:
            ChatMessage.objects.all().delete()
            return render(request, 'chat/chat.html', {'messages': [], "form": ChatMessageForm()})
    return render(request, 'chat/chat.html', {'messages': messages, "form": ChatMessageForm()})
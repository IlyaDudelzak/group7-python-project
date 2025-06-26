"""Views for the chat application."""

from django.shortcuts import render
from django.http import JsonResponse
import os
import google.generativeai as genai
from .forms import ChatMessageForm
from .models import ChatMessage
from contacts.models import Contact

def chat_view(request):
    """Render the chat interface."""
    messages = ChatMessage.objects.all()
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            # Save the message to the database
            ChatMessage.objects.create(
                role='user',
                content=form.cleaned_data['message']
            )

            user_message = form.cleaned_data['message']
            print(f"Received user message: {user_message}")
            if(user_message == ''):
                return JsonResponse({'error': 'Message cannot be empty'}, status=400)

            # Initialize Gemini
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                return JsonResponse({'error': 'API key not configured'}, status=500)

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))

            # Save user message
            ChatMessage.objects.create(
                role='user',
                content=user_message
            )

            # Prepare context for Gemini
            gemini_context = {}
            if request.user.is_authenticated:
                gemini_context['user'] = {
                    'username': request.user.username,
                    'email': request.user.email,
                }
                gemini_context['contacts'] = list(Contact.objects.filter(user=request.user).values('first_name', 'last_name', 'address', 'email', 'phone_number', 'birthday'))


            # Prepare Gemini request
            response = model.generate_content(user_message, context=gemini_context)

            # Save assistant message
            assistant_message = ChatMessage.objects.create(
                role='assistant',
                content=response.text
            )

            return render(request, 'chat/chat.html', {'messages': messages, "form": ChatMessageForm()})
        # Handle the 'Clear Chat' button functionality
        if request.method == 'POST' and 'clear_chat' in request.POST:
            ChatMessage.objects.all().delete()
            return render(request, 'chat/chat.html', {'messages': [], "form": ChatMessageForm()})
    return render(request, 'chat/chat.html', {'messages': messages, "form": ChatMessageForm()})


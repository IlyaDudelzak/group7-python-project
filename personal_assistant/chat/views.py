"""Views for the chat application."""

from django.shortcuts import render
from django.http import JsonResponse
import os
import google.generativeai as genai
from .models import ChatMessage

def chat_view(request):
    """Render the chat interface."""
    messages = ChatMessage.objects.all()
    return render(request, 'chat/chat.html', {'messages': messages})

def send_message(request):
    """Handle sending messages to the AI and receiving responses."""
    if request.method == 'POST':
        try:
            user_message = request.POST.get('message')
            if not user_message:
                return JsonResponse({'error': 'Message cannot be empty'}, status=400)

            # Initialize Gemini
            api_key = os.getenv('GOOGLE_API_KEY')
            if not api_key:
                return JsonResponse({'error': 'API key not configured'}, status=500)

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            # Save user message
            ChatMessage.objects.create(
                role='user',
                content=user_message
            )

            # Get AI response
            response = model.generate_content(user_message)

            # Save assistant message
            assistant_message = ChatMessage.objects.create(
                role='assistant',
                content=response.text
            )

            return JsonResponse({
                'message': response.text,
                'timestamp': assistant_message.timestamp.isoformat()
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

"""Implementation of the chat interface using Google's Gemini API."""

import os
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
from django.core.management.base import BaseCommand
from chat.models import ChatMessage

console = Console()

class Command(BaseCommand):
    """Django command to start the chat interface."""
    
    help = 'Start the AI chat interface'

    def handle(self, *args, **kwargs):
        """Execute the command."""
        try:
            api_key = os.getenv('GOOGLE_API_KEY')
            if not api_key:
                console.print("[red]Error: GOOGLE_API_KEY environment variable not set[/red]")
                return

            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            chat = model.start_chat(history=[])

            console.print("[bold blue]Welcome to AI Chat![/bold blue]")
            console.print("Type 'quit' or 'exit' to end the chat")
            console.print("Type 'clear' to clear chat history\n")

            while True:
                try:
                    user_input = input("You: ").strip()
                    
                    if user_input.lower() in ['quit', 'exit']:
                        console.print("\n[bold blue]Goodbye![/bold blue]")
                        break
                    
                    if not user_input:
                        continue
                        
                    if user_input.lower() == 'clear':
                        chat = model.start_chat(history=[])
                        ChatMessage.objects.all().delete()
                        console.print("[yellow]Chat history cleared[/yellow]\n")
                        continue

                    # Save user message
                    ChatMessage.objects.create(
                        role='user',
                        content=user_input
                    )

                    # Get AI response
                    response = chat.send_message(user_input)
                    
                    # Save assistant message
                    ChatMessage.objects.create(
                        role='assistant',
                        content=response.text
                    )

                    # Display response
                    console.print("\n[bold green]Assistant:[/bold green]")
                    console.print(Markdown(response.text))
                    console.print()

                except Exception as e:
                    console.print(f"\n[red]Error: {str(e)}[/red]\n")

        except KeyboardInterrupt:
            console.print("\n[bold blue]Chat ended by user[/bold blue]")

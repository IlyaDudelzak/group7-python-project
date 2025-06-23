"""
Console-based Gemini AI chat using google-generativeai.

- Requires: google-generativeai, rich
- Set GOOGLE_API_KEY as an environment variable
"""
import os
import sys
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

def main():
    """Run a console chat with Gemini AI."""
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("[ERROR] Please set the GOOGLE_API_KEY environment variable.")
        sys.exit(1)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    console = Console()

    console.print("[bold blue]Welcome to Gemini AI Chat![/bold blue]")
    console.print("Type 'exit' or 'quit' to leave. Type 'clear' to reset chat history.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                console.print("[bold blue]Goodbye![/bold blue]")
                break
            if user_input.lower() == "clear":
                chat = model.start_chat(history=[])
                console.print("[yellow]Chat history cleared.[/yellow]\n")
                continue
            # Send message to Gemini
            response = chat.send_message(user_input)
            console.print("\n[bold green]Gemini:[/bold green]")
            console.print(Markdown(response.text))
            console.print()
        except KeyboardInterrupt:
            console.print("\n[bold blue]Chat ended by user.[/bold blue]")
            break
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    main()
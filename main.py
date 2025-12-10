#!/usr/bin/env python3
# main.py - A simple AI agent using OpenRouter and OpenAI Python client
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

def main():
    """Main entry point for the AI agent."""
    print("AI Agent initialized!")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    # We seed our messages array with a system message to define the AI's personality. The user never sees this.
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. You are polite, creative, and concise."
        }
    ]

    while True:
        print("You can ask a question, give a command to generate a document, summarize text, and more.")
        print("Type 'exit' or 'quit' to end the session.\n")        
        user_input = input("> ")

        if user_input.lower() in ['exit', 'quit']:
            print("\nAI Response: Goodbye!")
            break 

        # Append user's new message to the history
        messages.append({"role": "user", "content": user_input})

        print("AI Response: Thinking...")
        
        completion = client.chat.completions.create(
            model="meta-llama/llama-3.3-70b-instruct:free",
            messages=messages 
        )
        response = completion.choices[0].message.content
        print("\n" + "="*40 + "\n" + "AI Response:", response, "\n" + "="*40 + "\n")

        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()

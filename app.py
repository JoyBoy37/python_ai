import gradio as gr
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Initialize the Anthropic client
# Get API key from environment variable
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def predict(message, history):
    # 2. Format the history for Claude's API
    # Claude expects a list of dictionaries with 'role' and 'content'
    messages = []
    for entry in history:
        if isinstance(entry, (list, tuple)) and len(entry) >= 2:
            messages.append({"role": "user", "content": entry[0]})
            messages.append({"role": "assistant", "content": entry[1]})
    
    # Add the current user message
    messages.append({"role": "user", "content": message})

    # 3. Call the Claude API
    response = client.messages.create(
        model="claude-haiku-4-5-20251001", # You can also use "claude-3-opus-20240229"
        max_tokens=1024,
        messages=messages
    )

    # 4. Return the text content
    return response.content[0].text

# 5. Create the Gradio Interface
demo = gr.ChatInterface(fn=predict, title="My Claude Assistant")

if __name__ == "__main__":
    demo.launch()
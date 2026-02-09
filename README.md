# python_ai

A Python project featuring Gradio-based AI applications powered by Anthropic's Claude API.

## Project Structure

- **app.py** - Main Claude chatbot application with conversation history support using Gradio
- **app0.py** - Basic Gradio interface example with greeting functionality
- **requirements.txt** - Python dependencies
- **.gitignore** - Git ignore configuration for Python projects

## Features

### app.py - Claude Chat Assistant
- Interactive chatbot interface using Gradio
- Integrates with Anthropic's Claude Haiku API
- Maintains conversation history
- Environment variable configuration via .env file

### app0.py - Simple Greeting App
- Basic Gradio interface example
- Text input and slider controls
- Share-enabled deployment

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

4. Run the application:
   - For Claude chatbot: `python app.py`
   - For greeting app: `python app0.py`

## Environment Variables

- `ANTHROPIC_API_KEY` - Your Anthropic API key (stored in .env file)
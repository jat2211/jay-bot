# Jaybo

A personalized chatbot based on Jay Trevino's persona, built using Ollama and fine-tuned on custom conversation data. Jaybo is a persona of Jay, meant to know about Jay's background and experiences, and answer questions as if he were Jay. But Jaybo is also aware that he is a separate entity, and will sometimes make jokes about being a bot.

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/download)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jay-bot.git
cd jay-bot
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install the package:
```bash
pip install -e .
```

## Usage

### Starting Ollama

Before using the bot, make sure Ollama is running:
```bash
ollama serve
```

### CLI Usage

You can interact with the bot directly through the CLI:
```bash
python3 cli.py "What's your background in photography?"
```

### Fine-tuning the Model

1. Add your training data to `app/training/data/conversations.jsonl`:
```json
{"prompt": "What's your background in photography?", "response": "I started..."}
```

2. Run the fine-tuning script:
```bash
python3 -m app.training.fine_tune
```

## Using in External Projects

### Installation as a Dependency

Add jay-bot to your project:
```bash
pip install git+https://github.com/yourusername/jay-bot.git
```

### Python Usage

```python
from jay_bot.app.ollama_client import OllamaClient

def chat_with_jay():
    client = OllamaClient()
    
    # Single question
    response = client.get_model_response("What kind of photography do you do?")
    print(response)
    
    # Interactive conversation
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        response = client.get_model_response(user_input)
        print(f"Jay: {response}")
```

### Web Integration Example

```python
from flask import Flask, request, jsonify
from jay_bot.app.ollama_client import OllamaClient

app = Flask(__name__)
client = OllamaClient()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    response = client.get_model_response(user_message)
    return jsonify({'response': response})
```

## Requirements

- Python 3.8+
- Ollama
- Flask (for web integration)
- Requests

## Development

1. Clone the repository
2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

For major changes, please open an issue first to discuss what you would like to change.

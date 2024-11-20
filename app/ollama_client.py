import requests

class OllamaClient:
    def __init__(self):
        # Local Ollama server URL
        self.model_url = 'http://localhost:11434/models/llama2'  # Update to your model name

    def get_model_response(self, user_input):
        # Send user input to the local Ollama model and receive a response
        try:
            response = requests.post(self.model_url, json={"input": user_input})
            if response.status_code == 200:
                return response.json().get('response', 'No response from model.')
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"

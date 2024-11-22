import requests

class OllamaClient:
    def __init__(self):
        self.base_url = "http://localhost:11434/api"
        self.model = "jaybo"  # Use your fine-tuned model

    def get_model_response(self, prompt):
        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            return response.json()["response"]
        except Exception as e:
            return f"Error: {str(e)}"

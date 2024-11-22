import sys
import requests
from app.ollama_client import OllamaClient

def is_ollama_running():
    try:
        response = requests.get('http://localhost:11434/api/version')
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def main():
    if not is_ollama_running():
        print("Please start Ollama by running: ollama serve")
        sys.exit(1)

    ollama_client = OllamaClient()

    # check if user input passed as an arg
    if len(sys.argv) < 2:
        print("please talk to me")
        sys.exit(1)

    try:
        # get user input from cli arguments
        user_input = " ".join(sys.argv[1:])

        # get model's response
        response = ollama_client.get_model_response(user_input)
        print(response)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

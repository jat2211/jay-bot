import sys
from app.ollama_client import OllamaClient

def main():
    ollama_client = OllamaClient()

    # check if user input passed as an arg
    if len(sys.argv) < 2:
        print("please talk to me")
        sys.exit(1)

    # get user input from cli arguments
    user_input = " ".join(sys.argv[1:])

    # get model's response
    response = ollama_client.get_model_response(user_input)
    print(response)

if __name__ == "__main__":
    main()

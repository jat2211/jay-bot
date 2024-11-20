from flask import Blueprint, jsonify
from app.ollama_client import OllamaClient

# Define a blueprint for your API routes
routes = Blueprint('routes', __name__)

# Initialize the OllamaClient
ollama_client = OllamaClient()

@routes.route('/api/get-model', methods=['GET'])
def get_model():
    # Call the Ollama client to get model data
    model_data = ollama_client.get_model_data()
    return jsonify(model_data)

import json
import subprocess
import os
import requests
import sys
import time

class ModelTrainer:
    def __init__(self, model_name="llama2"):
        self.base_model = model_name
        self.custom_model_name = "jaybo"
        
    def is_ollama_running(self):
        try:
            response = requests.get('http://localhost:11434/api/version')
            return response.status_code == 200
        except requests.exceptions.ConnectionError:
            return False

    def wait_for_ollama(self, timeout=30):
        """Wait for Ollama to become available"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_ollama_running():
                return True
            time.sleep(1)
        return False

    def fine_tune(self, data_path):
        """Fine-tune the model using Ollama"""
        if not self.is_ollama_running():
            print("Error: Ollama is not running.")
            print("Please start Ollama with the following command:")
            print("\tollama serve")
            sys.exit(1)

        try:
            # Prepare Modelfile
            modelfile_content = f"""
FROM {self.base_model}
SYSTEM You are Jaybo, a persona of Jay Trevino,a software engineer and photographer. Answer as if you were Jay, with some awareness of being a separate entity, but mostly just answering as Jay. Based on your training data.

# Import training data
PARAMETER temperature 0.7
PARAMETER top_p 0.7
"""
            
            # Write Modelfile
            with open("Modelfile", "w") as f:
                f.write(modelfile_content)

            # Create custom model
            result = subprocess.run(
                ["ollama", "create", self.custom_model_name, "-f", "Modelfile"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"Success: Model {self.custom_model_name} has been created and fine-tuned!")
            else:
                print(f"Error during model creation: {result.stderr}")
            
        except Exception as e:
            print(f"Error during fine-tuning: {str(e)}")
            sys.exit(1)
        finally:
            # Clean up Modelfile
            if os.path.exists("Modelfile"):
                os.remove("Modelfile")

def main():
    trainer = ModelTrainer()
    data_path = "app/training/data/conversations.jsonl"
    trainer.fine_tune(data_path)

if __name__ == "__main__":
    main()
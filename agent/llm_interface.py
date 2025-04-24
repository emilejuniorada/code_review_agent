import requests

class OllamaAPI:
    def __init__(self, model_name: str, base_url: str = "http://localhost:11434/api"):
        """
        Initialize the OllamaAPI with the specified model name and base URL.
        """
        self.model_name = model_name
        self.base_url = base_url

    def query(self, prompt: str) -> dict:
        """
        Send a query to the Ollama API with the given prompt and return the response.
        """
        url = f"{self.base_url}/generate"
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
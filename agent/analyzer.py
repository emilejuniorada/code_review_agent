import os
import sys
import yaml
from agent.llm_interface import OllamaAPI

class CodeAnalyzer:
    def __init__(self, model_name="deepseek-coder", mode="strict", config_path="prompts/template.yml"):
        """
        Initialize the CodeAnalyzer with the specified model, mode, and configuration.
        """
        self.model_name = model_name
        self.mode = mode
        self.config = self._load_config(config_path)
        self.api = OllamaAPI(model_name)

    def _load_config(self, config_path: str) -> dict:
        """
        Load the configuration file for modes and providers.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
        
        with open(config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def analyze_file(self, file_path: str) -> str:
        """
        Analyze the Python code in the specified file and return a review.
        """
        if not os.path.exists(file_path):
            return f"Error: File '{file_path}' does not exist."

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                code = file.read()
        except Exception as e:
            return f"Error reading file: {e}"

        return self.analyze_code(code)

    def analyze_code(self, code: str) -> str:
        """
        Analyze the provided Python code and return a review.
        """
        prompt = self._construct_prompt(code)
        response = self.api.query(prompt)
        return self._parse_response(response)

    def _construct_prompt(self, code: str) -> str:
        """
        Construct the prompt to send to the LLM for code analysis based on the mode.
        """
        if self.mode not in self.config["modes"]:
            raise ValueError(f"Invalid mode '{self.mode}'. Supported modes: {list(self.config['modes'].keys())}")

        prompt_template = self.config["modes"][self.mode]["prompt_template"]
        return prompt_template.replace("{code}", code)

    def _parse_response(self, response: str) -> str:
        """
        Parse the response from the LLM and extract the review text.
        """
        return response["response"]

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python analyzer.py <path_to_python_file> <mode>")
        sys.exit(1)

    file_path = sys.argv[1]
    mode = sys.argv[2]

    analyzer = CodeAnalyzer(mode=mode)
    review = analyzer.analyze_file(file_path)
    print("Code Review:")
    print(review)
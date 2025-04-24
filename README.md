# Project Name

This project is designed to facilitate the analysis and review of scripts using language models. It includes various components that work together to provide a unified interface for interacting with language models, as well as tools for constructing prompts and reviewing outputs.

## Project Structure

- **agent/**: Contains the core logic for analyzing scripts and interfacing with language models.
  - `analyzer.py`: Implements the review logic and prompt construction.
  - `llm_interface.py`: Provides a unified API for interacting with language models, including an abstraction for the Ollama interface.

- **examples/**: Contains example scripts to demonstrate the functionality of the project.
  - `buggy_script.py`: An example script with intentional bugs for testing purposes.
  - `clean_script.py`: A clean example script demonstrating proper usage.

- **prompts/**: Stores different prompt styles in YAML format.
  - `templates.yaml`: Defines various templates for generating prompts.

- **reviews/**: Stores the output of reviews conducted by the analyzer.
  - `review_output.md`: Contains formatted text summarizing the results of the reviews.

- **cli.py**: The command-line runner for the project, handling user input and executing main features.

- **config.yaml**: Configuration file for API keys and model settings.

- **requirements.txt**: Lists the dependencies required to run the project.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the command-line interface, use:

```
python cli.py [options]
```

Refer to the documentation within the CLI for available options and commands.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
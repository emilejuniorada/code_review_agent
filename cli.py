import argparse
import os
from agent.analyzer import CodeAnalyzer

def save_review_to_file(review: str, file_path: str, mode: str):
    """
    Save the review result to a Markdown file inside the 'reviews' folder.
    """
    reviews_folder = "reviews"
    os.makedirs(reviews_folder, exist_ok=True)

    review_file_path = os.path.join(reviews_folder, "review_output.md")

    try:
        with open(review_file_path, "w", encoding="utf-8") as review_file:
            review_file.write(f"# Code Review ({mode.capitalize()} Mode)\n\n")
            review_file.write(review)
        print(f"Review saved to: {review_file_path}")
    except Exception as e:
        print(f"Error saving review to file: {e}")

def main():
    """
    Entry point for the CLI tool.
    """
    parser = argparse.ArgumentParser(description="Analyze Python code using an AI code reviewer.")
    parser.add_argument("--file", required=True, help="Path to the Python file to analyze.")
    parser.add_argument("--mode", choices=["strict", "mentor", "test_focus"], default="strict", 
                        help="Review mode: 'strict' for detailed analysis, 'mentor' for constructive feedback, 'test_focus' for test coverage analysis.")
    parser.add_argument("--provider", choices=["ollama"], default="ollama", 
                        help="LLM provider to use for analysis (default: ollama).")

    args = parser.parse_args()

    file_path = args.file
    mode = args.mode
    provider = args.provider

    if provider != "ollama":
        print(f"Error: Unsupported provider '{provider}'. Currently, only 'ollama' is supported.")
        return

    analyzer = CodeAnalyzer(mode=mode)

    print(f"Analyzing file: {file_path} (Mode: {mode}, Provider: {provider})")
    review = analyzer.analyze_file(file_path)

    # Save the review to a Markdown file
    save_review_to_file(review, file_path, mode)

if __name__ == "__main__":
    main()
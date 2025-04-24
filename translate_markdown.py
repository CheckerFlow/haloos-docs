import os
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Directory containing the Markdown files
input_dir = "./"  # Adjust to your repo's root directory
output_dir = "./translated_docs"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def translate_markdown(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        # Translate the content
        translated = translator.translate(content, src='zh-cn', dest='en').text

        # Save the translated content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated)
    except Exception as e:
        print(f"Error translating {file_path}: {e}")

def process_markdown_files():
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".md"):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)

                # Ensure the output subdirectory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                print(f"Translating: {input_path} -> {output_path}")
                translate_markdown(input_path, output_path)

if __name__ == "__main__":
    process_markdown_files()
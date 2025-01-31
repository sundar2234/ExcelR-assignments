import re
from collections import Counter

def load_text_file(file_path):
    """Loads the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def tokenize(text):
    """Tokenizes text by splitting on non-alphanumeric characters."""
    tokens = re.findall(r'\b\w+\b', text.lower())  # Convert to lowercase and extract words
    return tokens

def compute_term_frequency(tokens):
    """Computes term frequency (TF) of tokens."""
    return Counter(tokens)

def main():
    file_path = 'sample.txt'  # Replace with your file path
    text = load_text_file(file_path)
    tokens = tokenize(text)
    term_freq = compute_term_frequency(tokens)
    
    print("Top 5 most frequent tokens:")
    for token, freq in term_freq.most_common(5):
        print(f"{token}: {freq}")

if __name__ == "__main__":
    main()

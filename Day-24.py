import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def tokenize_text(text):
    tokens = word_tokenize(text.lower())
    return tokens

def filter_tokens(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return filtered_tokens

def get_most_common_words(tokens, num_words=10):
    word_counts = Counter(tokens)
    most_common_words = word_counts.most_common(num_words)
    return most_common_words

def main():
    file_path = 'your_text_file.txt'  # Replace with your text file path
    text = load_text(file_path)
    tokens = tokenize_text(text)
    filtered_tokens = filter_tokens(tokens)
    most_common_words = get_most_common_words(filtered_tokens)
    
    print("The 10 most common words are:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
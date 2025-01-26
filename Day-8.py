import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')

def tokenize_paragraph(paragraph):
    """Tokenizes a paragraph into sentences and words."""
    sentences = sent_tokenize(paragraph)
    words = word_tokenize(paragraph)
    return sentences, words

# Sample paragraph
paragraph = "Natural language processing (NLP) is a sub-field of artificial intelligence. It focuses on the interaction between computers and human language. Tokenization is a key step in NLP!"

# Tokenize the paragraph
sentences, words = tokenize_paragraph(paragraph)

# Display the results
print("Sentences:")
print(sentences)
print("\nWords:")
print(words)

# Save results to a file
def save_to_file(sentences, words, filename="tokenized_output.txt"):
    with open(filename, "w") as file:
        file.write("Sentences:\n")
        file.writelines(f"- {sentence}\n" for sentence in sentences)
        file.write("\nWords:\n")
        file.writelines(f"- {word}\n" for word in words)
    print(f"Results saved to {filename}")

save_to_file(sentences, words)

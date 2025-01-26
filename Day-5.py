
from collections import Counter

def calculate_word_frequency(text):

    text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    
    words = text.split()
    
    word_count = Counter(words)
    return word_count


text = input("Enter the text: ")


word_frequencies = calculate_word_frequency(text)


print("\nWord Frequencies:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")

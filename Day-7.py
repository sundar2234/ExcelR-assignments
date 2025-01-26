
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string, strip_punctuation, strip_numeric, stem_text
from nltk.stem import WordNetLemmatizer
import nltk


nltk.download('wordnet')
nltk.download('omw-1.4')


def preprocess_text(text):
  
    text = remove_stopwords(text)
 
    filters = [strip_punctuation, strip_numeric, lambda x: x.lower(), stem_text]
    text = preprocess_string(text, filters)
    
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(word) for word in text]
    
    return lemmatized_text

file_path = input("Enter the path to the sample text file: ")
try:
    with open(file_path, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("File not found. Please provide a valid path.")
    exit()


processed_text = preprocess_text(text)


print("\nPreprocessed Text:")
print(" ".join(processed_text))

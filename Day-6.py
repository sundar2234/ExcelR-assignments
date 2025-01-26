
import nltk
from nltk.corpus import stopwords
import spacy


nltk.download('stopwords')


def process_text(text):
   
    text = text.lower()
    
    
    stop_words = set(stopwords.words('english'))
    
   
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    

    filtered_words = [token.text for token in doc if token.text not in stop_words]
    
    return filtered_words


text = input("Enter the text: ")


processed_words = process_text(text)


print("\nProcessed Words:")
print(" ".join(processed_words))

import spacy

# Load the English model from SpaCy
nlp = spacy.load("en_core_web_sm")

# Define the sentence
sentence = "NLP is amazing and fun to learn."

# Process the sentence with the SpaCy pipeline
doc = nlp(sentence)

# Print each token with its part of speech tag
print(f"{'Token':<10} {'POS Tag':<10} {'POS Description'}")
print("-" * 35)
for token in doc:
    print(f"{token.text:<10} {token.pos_:<10} {spacy.explain(token.pos_)}")

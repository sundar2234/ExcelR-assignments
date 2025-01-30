import spacy

# Load SpaCy's English model
nlp = spacy.load("en_core_web_sm")

# Sample text for NER
text = """
Apple is looking to buy a startup in the UK for $1 billion. 
Tim Cook, the CEO of Apple, announced the deal on January 25, 2025.
"""

# Process the text using SpaCy
doc = nlp(text)

# Print the entities and their types
for entity in doc.ents:
    print(f"Entity: {entity.text}, Type: {entity.label_}")

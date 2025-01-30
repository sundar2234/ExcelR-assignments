from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity[0][0]

# Example usage
text1 = "Machine learning is amazing."
text2 = "Machine learning is incredible."

similarity_score = calculate_cosine_similarity(text1, text2)
print(f"Cosine Similarity: {similarity_score:.4f}")
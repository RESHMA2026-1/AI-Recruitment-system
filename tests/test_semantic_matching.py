from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = "Machine Learning Python Data Science"
jd = "AI Python Data Science"

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([resume, jd])

score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

print("Similarity Score:", score)
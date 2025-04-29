from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from .preprocessing import preprocess
import numpy as np

class LSISearch:
    def __init__(self, documents, n_components=50):
        self.documents = documents
        self.titles = list(documents.keys())
        self.n_components = n_components
        self._prepare_lsi()

    def _prepare_lsi(self):
        corpus = [preprocess(doc) for doc in self.documents.values()]
        self.vectorizer = TfidfVectorizer()
        X_tfidf = self.vectorizer.fit_transform(corpus)
        self.svd = TruncatedSVD(n_components=self.n_components, random_state=42)
        self.X_lsi = self.svd.fit_transform(X_tfidf)


    def search(self, query):
            """Performs LSI-based search."""
            query = preprocess(query)
            query_vec = self.vectorizer.transform([query])
            query_lsi = self.svd.transform(query_vec)

            # Compute cosine similarities
            similarities = np.dot(self.X_lsi, query_lsi.T).flatten()

            # Remove results where similarity is 0.000000 (or close to 0)
            results = [(self.titles[idx], similarities[idx]) for idx in range(len(similarities)) if similarities[idx] > 0.0001]

            # Rank documents by similarity (highest first)
            results = sorted(results, key=lambda x: x[1], reverse=True)

            return results